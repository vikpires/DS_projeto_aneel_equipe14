from pathlib import Path

# Configuração de diretórios relativos
SRC_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SRC_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"
SQL_DIR = PROJECT_ROOT / "src" / "sql"


# URLs e informações do repositório
REPO_NAME = "projeto_aneel_equipe14"
REPO_URL = "https://github.com/vikpires/projeto_aneel_equipe14"
TAG_RELEASE = "v0.1.0"
RELEASE_BASE_URL = f"{REPO_URL}/releases/download/{TAG_RELEASE}"

# Configuração de arquivos padrão e paths
PROCESSED_RELEASE_FILES = ["fato_dimensao_2021_2025.zip"]
CONT_PATH = INTERIM_DIR / "continuidade_2021_2025.parquet"
INT_PATH = INTERIM_DIR / "interrupcoes_2021_2025.parquet"
LIM_PATH = INTERIM_DIR / "limites_2021_2025.parquet"
ATR_PATH = INTERIM_DIR / "atributos.parquet"
REG_PATH = INTERIM_DIR / "regiao.parquet"

# Base de dados do projeto
URL_BASE_CONTINUIDADE = "https://dadosabertos.aneel.gov.br/dataset/d5f0712e-62f6-4736-8dff-9991f10758a7/resource/d7f70fb1-725c-4748-afeb-65c6a78df550/download/indicadores-continuidade-coletivos-2020-2029.parquet"
URL_BASE_INTERRUPCOES = {
    2021: "https://dadosabertos.aneel.gov.br/dataset/ccb25653-f07b-4f28-84c2-62a89d1f5a56/resource/011e0086-8b2f-4fbc-a32b-f7c0f7bc9957/download/interrupcoes-energia-eletrica-2021.parquet",
    2022: "https://dadosabertos.aneel.gov.br/dataset/ccb25653-f07b-4f28-84c2-62a89d1f5a56/resource/f40b948c-81a3-4d56-8e35-0af9c2533178/download/interrupcoes-energia-eletrica-2022.parquet",
    2023: "https://dadosabertos.aneel.gov.br/dataset/ccb25653-f07b-4f28-84c2-62a89d1f5a56/resource/ddc26540-cd8c-4eef-a1ad-a234d24ed9c4/download/interrupcoes-energia-eletrica-2023.parquet",
    2024: "https://dadosabertos.aneel.gov.br/dataset/ccb25653-f07b-4f28-84c2-62a89d1f5a56/resource/fc5ca52c-329c-4443-a2d6-08ccec711ade/download/interrupcoes-energia-eletrica-2024.parquet",
    2025: "https://dadosabertos.aneel.gov.br/dataset/ccb25653-f07b-4f28-84c2-62a89d1f5a56/resource/691de320-cb3d-471b-b9ec-8c1b86af8c83/download/interrupcoes-energia-eletrica-2025.parquet",
}
URL_BASE_LIMITES = "https://dadosabertos.aneel.gov.br/dataset/d5f0712e-62f6-4736-8dff-9991f10758a7/resource/fd69e1dd-fd66-4269-b60c-cc0b7eb221b4/download/indicadores-continuidade-coletivos-limite.csv"
URL_BASE_ATRIBUTOS = "https://dadosabertos.aneel.gov.br/dataset/d5f0712e-62f6-4736-8dff-9991f10758a7/resource/3c780aca-38cf-406d-9d45-f07a9216eef2/download/indicadores-continuidade-coletivos-atributos.csv"
URL_BASE_REGIAO = "https://dadosabertos.aneel.gov.br/dataset/db9c9f60-b3b5-4504-9dfe-2637922d53ce/resource/3f841488-80a8-42f2-a6ca-e0c593b228de/download/indqual-municipio.csv"


# Configuração das fontes, transformações e destinos do pipeline.
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
    "limites": {
        "url": URL_BASE_LIMITES,
        "query_name": "filter_limites",
        "raw_path": RAW_DIR / "raw_limites.csv",
        "out_path": LIM_PATH,
    },
    "atributos": {
        "url": URL_BASE_ATRIBUTOS,
        "query_name": "filter_atributos",
        "raw_path": RAW_DIR / "raw_atributos.csv",
        "out_path": ATR_PATH,
    },
    "regiao": {
        "url": URL_BASE_REGIAO,
        "query_name": "filter_regiao",
        "raw_path": RAW_DIR / "raw_regiao.csv",
        "out_path": REG_PATH,
    },
}
