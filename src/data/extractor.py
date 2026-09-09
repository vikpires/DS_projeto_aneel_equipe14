import requests
import os
import tempfile
from pathlib import Path

from src.config import RAW_DIR, setup_folders
from src.data.constants import DATASETS


# Função para realizar o download em stream da base de dados, evitando sobrecarga de memória.
def download_stream(url: str, dest_path: Path | str):
    dest_path = Path(dest_path)
    if dest_path.exists():
        print(f"[CACHE] Arquivo já existe: {dest_path.name}")
        return

    print(f"[DOWNLOAD] Iniciando download: {dest_path.name}...")
    headers = {"User-Agent": "Mozilla/5.0"}
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

        with requests.get(url, headers=headers, stream=True, timeout=120) as response:
            response.raise_for_status()
            with temporary_path.open("wb") as output_file:
                for chunk in response.iter_content(chunk_size=1024 * 1024 * 10):
                    if chunk:
                        output_file.write(chunk)

        os.replace(temporary_path, dest_path)
    except Exception:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise
    print(f"[DOWNLOAD] Concluído: {dest_path.name}")


# Executar o processo de ingestão de dados.
def run_extract_data():

    setup_folders()

    # 1. Download do Arquivo Raw de Continuidade (arquivo único)
    print("\n--- Baixando Dataset de Continuidade ---")
    download_stream(
        DATASETS["continuidade"]["url"], DATASETS["continuidade"]["raw_path"]
    )

    # 2. Download dos Arquivos Raw de Interrupções (em lote por ano)
    print("\n--- Baixando Datasets de Interrupções (2021 a 2025) ---")
    for ano, url in DATASETS["interrupcoes"]["urls"].items():
        destino_ano = RAW_DIR / f"raw_interrupcoes_{ano}.parquet"
        print(f"-> Baixando base de {ano}...")
        download_stream(url, destino_ano)
