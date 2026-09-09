from src.config import (
    RAW_DIR,
    URL_BASE_CONTINUIDADE,
    URL_BASE_INTERRUPCOES,
    CONT_PATH,
    INT_PATH,
)

# Define a estrutura de diretórios e URLs para os datasets do projeto
DATASETS = {
    "continuidade": {
        "url": URL_BASE_CONTINUIDADE,
        "query_name": "filter_continuidade",
        "raw_path": RAW_DIR / "raw_continuidade.parquet",
        "out_path": CONT_PATH,
    },
    "interrupcoes": {
        "urls": URL_BASE_INTERRUPCOES,
        "query_name": "filter_interrupcoes",
        "raw_pattern": RAW_DIR / "raw_interrupcoes_*.parquet",
        "out_path": INT_PATH,
    },
}
