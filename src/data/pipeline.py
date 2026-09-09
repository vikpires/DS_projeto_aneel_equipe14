from src.data.extractor import run_extract_data
from src.data.transformer import run_transform_data
from src.data.validator import run_validation


# Orquestrador local de download, processamento e validação de qualidade dos datasets.
def run_pipeline():

    # 1. Ingestão de dados
    run_extract_data()

    # 2. Processamento via DuckDB
    run_transform_data()

    # 3. Validação de qualidade dos dados
    run_validation()


if __name__ == "__main__":
    run_pipeline()
