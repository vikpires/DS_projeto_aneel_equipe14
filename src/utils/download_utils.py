import logging
import os
import tempfile
import zipfile
from pathlib import Path
import requests

logger = logging.getLogger(__name__)


# Baixa um arquivo em streaming usando um arquivo temporário atômico.
def download_stream(
    url: str,
    dest_path: Path | str,
    force: bool = False,
) -> None:
    dest_path = Path(dest_path)
    if dest_path.is_file() and dest_path.stat().st_size > 0 and not force:
        logger.info("[CACHE] Arquivo já existe: %s", dest_path.name)
        return

    dest_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = None
    try:
        with tempfile.NamedTemporaryFile(
            dir=dest_path.parent,
            prefix=f".{dest_path.name}.",
            suffix=".part",
            delete=False,
        ) as temporary_file:
            temporary_path = Path(temporary_file.name)

        logger.info("[DOWNLOAD] Iniciando download: %s...", dest_path.name)
        with requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            stream=True,
            timeout=120,
        ) as response:
            response.raise_for_status()
            expected_size = response.headers.get("Content-Length")
            downloaded_size = 0
            with temporary_path.open("wb") as output_file:
                for chunk in response.iter_content(chunk_size=1024 * 1024 * 10):
                    if chunk:
                        output_file.write(chunk)
                        downloaded_size += len(chunk)

        if downloaded_size == 0:
            raise ValueError(f"Download vazio recebido de {url}")
        if expected_size is not None and downloaded_size != int(expected_size):
            raise ValueError(
                f"Tamanho inesperado para {url}: "
                f"esperado {expected_size}, recebido {downloaded_size}"
            )

        os.replace(temporary_path, dest_path)
        logger.info("[DOWNLOAD] Concluído: %s", dest_path.name)
    except Exception:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise


# Baixa um asset e extrai ZIPs com proteção contra Zip Slip.
def download_and_extract(
    base_url: str,
    asset_name: str,
    destination_dir: Path | str,
    force: bool = False,
) -> list[Path]:
    destination_dir = Path(destination_dir)
    destination_dir.mkdir(parents=True, exist_ok=True)
    archive_path = destination_dir / asset_name
    url = f"{base_url.rstrip('/')}/{asset_name}"

    download_stream(url, archive_path, force=force)
    if archive_path.suffix.lower() != ".zip":
        return [archive_path]

    destination_root = destination_dir.resolve()
    with zipfile.ZipFile(archive_path) as archive:
        for member in archive.infolist():
            member_path = (destination_dir / member.filename).resolve()
            if destination_root not in member_path.parents:
                raise ValueError(f"Caminho inseguro no ZIP: {member.filename}")
        archive.extractall(destination_dir)
        extracted_files = [
            destination_dir / member.filename
            for member in archive.infolist()
            if not member.is_dir()
        ]

    logger.info("[SUCESSO] Extraído: %s", asset_name)
    return extracted_files
