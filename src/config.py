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
TAG_RELEASE = "v0.1.0-data"
RELEASE_BASE_URL = f"{REPO_URL}/releases/download/{TAG_RELEASE}"

# Configuração de arquivos padrão e paths
DEFAULT_FILES = ["continuidade_2021_2025.parquet", "interrupcoes_2021_2025.parquet"]
CONT_PATH = (INTERIM_DIR / DEFAULT_FILES[0]).as_posix()
INT_PATH = (INTERIM_DIR / DEFAULT_FILES[1]).as_posix()

# Período de análise do projeto
ANO_INICIO = 2021
ANO_FIM = 2025

# Base de dados do projeto
URL_BASE_CONTINUIDADE = "https://dadosabertos.aneel.gov.br/dataset/d5f0712e-62f6-4736-8dff-9991f10758a7/resource/d7f70fb1-725c-4748-afeb-65c6a78df550/download/indicadores-continuidade-coletivos-2020-2029.parquet"
URL_BASE_INTERRUPCOES = {
    2021: "https://dadosabertos.aneel.gov.br/dataset/ccb25653-f07b-4f28-84c2-62a89d1f5a56/resource/011e0086-8b2f-4fbc-a32b-f7c0f7bc9957/download/interrupcoes-energia-eletrica-2021.parquet",
    2022: "https://dadosabertos.aneel.gov.br/dataset/ccb25653-f07b-4f28-84c2-62a89d1f5a56/resource/f40b948c-81a3-4d56-8e35-0af9c2533178/download/interrupcoes-energia-eletrica-2022.parquet",
    2023: "https://dadosabertos.aneel.gov.br/dataset/ccb25653-f07b-4f28-84c2-62a89d1f5a56/resource/ddc26540-cd8c-4eef-a1ad-a234d24ed9c4/download/interrupcoes-energia-eletrica-2023.parquet",
    2024: "https://dadosabertos.aneel.gov.br/dataset/ccb25653-f07b-4f28-84c2-62a89d1f5a56/resource/fc5ca52c-329c-4443-a2d6-08ccec711ade/download/interrupcoes-energia-eletrica-2024.parquet",
    2025: "https://dadosabertos.aneel.gov.br/dataset/ccb25653-f07b-4f28-84c2-62a89d1f5a56/resource/691de320-cb3d-471b-b9ec-8c1b86af8c83/download/interrupcoes-energia-eletrica-2025.parquet",
}


# Criação automática dos diretórios se não existirem
def setup_folders():
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    INTERIM_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
