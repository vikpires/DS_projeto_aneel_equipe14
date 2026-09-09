import os
import tempfile
import urllib.request
from pathlib import Path
from typing import List, Optional
from src.config import RELEASE_BASE_URL, INTERIM_DIR, DEFAULT_FILES


# Função para baixar arquivos .parquet da Release do GitHub para a pasta data/interim/
def fetch_data(files: Optional[List[str]] = None, force: bool = False) -> None:
    files_to_download = files or DEFAULT_FILES
    os.makedirs(INTERIM_DIR, exist_ok=True)

    for file_name in files_to_download:
        dest_path = Path(INTERIM_DIR) / file_name

        if dest_path.exists() and not force:
            print(f"[CACHE] {file_name} já existe em interim. Pulando...")
            continue

        file_url = f"{RELEASE_BASE_URL}/{file_name}"
        print(f"[DOWNLOAD] Baixando {file_name} da Release...")
        temporary_path = None

        try:
            with tempfile.NamedTemporaryFile(
                dir=dest_path.parent,
                prefix=f".{dest_path.name}.",
                suffix=".part",
                delete=False,
            ) as temporary_file:
                temporary_path = Path(temporary_file.name)

            urllib.request.urlretrieve(file_url, temporary_path)
            os.replace(temporary_path, dest_path)
            print(f"[SUCESSO] Salvo em: {dest_path}")

        except Exception as error:
            print(f"[ERRO] Falha ao baixar {file_name} de {file_url}: {error}")
            if temporary_path is not None:
                temporary_path.unlink(missing_ok=True)
            raise RuntimeError(f"Falha ao baixar {file_name} de {file_url}") from error
