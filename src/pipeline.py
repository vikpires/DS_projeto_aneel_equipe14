import logging

from src.data.extractor import run_extract_data
from src.data.transformer import run_transform_data
from src.data.fato_dim import run_fato_dim
from src.data.quality_raw import validate_raw_tables
from src.data.quality_interim import validate_interim_tables
from src.data.quality_processed import validate_processed_tables


# Orquestrador local do pipeline de download, processamento, validação de qualidade dos datasets e modelagem dimensional.
def run_pipeline() -> None:

    # 1. Ingestão de dados
    run_extract_data()

    # 2. Quality gate das fontes brutas
    validate_raw_tables()

    # 3. Processamento via DuckDB
    run_transform_data()

    # 4. Quality gate dos dados intermediários
    validate_interim_tables()

    # 5. Geração do modelo dimensional (fato e dimensões)
    run_fato_dim()

    # 6. Quality gate dos artefatos finais
    validate_processed_tables()


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    run_pipeline()
