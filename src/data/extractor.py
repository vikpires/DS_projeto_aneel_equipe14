import logging

from src.config import DATASETS, INTERIM_DIR, PROCESSED_DIR, RAW_DIR
from src.utils.download_utils import download_stream

logger = logging.getLogger(__name__)


# Função para criar os diretórios necessários caso não existam
def setup_folders() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    INTERIM_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


# Executar o processo de ingestão de dados.
def run_extract_data() -> None:

    setup_folders()

    # 1. Download do Arquivo Raw de Continuidade (arquivo único)
    logger.info("--- Baixando Dataset de Continuidade ---")
    download_stream(
        DATASETS["continuidade"]["url"], DATASETS["continuidade"]["raw_path"]
    )

    # 2. Download dos Arquivos Raw de Interrupções (em lote por ano)
    logger.info("--- Baixando Datasets de Interrupções (2021 a 2025) ---")
    for ano, url in DATASETS["interrupcoes"]["urls"].items():
        destino_ano = RAW_DIR / f"raw_interrupcoes_{ano}.parquet"
        logger.info("-> Baixando base de %s...", ano)
        download_stream(url, destino_ano)

    # 3. Download do Arquivo Raw de Limites (arquivo único)
    logger.info("--- Baixando Dataset de Limites ---")
    download_stream(DATASETS["limites"]["url"], DATASETS["limites"]["raw_path"])

    # 4. Download do Arquivo Raw de Atributos (arquivo único)
    logger.info("--- Baixando Dataset de Atributos ---")
    download_stream(DATASETS["atributos"]["url"], DATASETS["atributos"]["raw_path"])

    # 5. Região e UF dos conjuntos
    logger.info("--- Baixando Dataset de Região ---")
    download_stream(DATASETS["regiao"]["url"], DATASETS["regiao"]["raw_path"])


if __name__ == "__main__":
    run_extract_data()
