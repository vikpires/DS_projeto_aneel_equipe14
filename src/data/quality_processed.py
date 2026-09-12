import json
import logging
from pathlib import Path
import duckdb

from src.config import PROCESSED_DIR
from src.data.constants import PIPELINE_TABLES

logger = logging.getLogger(__name__)


# Valida o contrato dos Parquets finais gerados pelo Star Schema.
def validate_processed_tables(output_dir: Path | str = PROCESSED_DIR) -> None:
    output_dir = Path(output_dir)
    if not output_dir.is_dir():
        raise FileNotFoundError(f"Diretório processado ausente: {output_dir}")

    manifest_path = output_dir / "_manifesto.json"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Manifesto ausente: {manifest_path}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("status") != "SUCCESS":
        raise ValueError("Manifesto do Star Schema não indica sucesso")

    expected_files = {f"{table}.parquet" for table in PIPELINE_TABLES}
    missing_files = sorted(
        file_name
        for file_name in expected_files
        if not (output_dir / file_name).is_file()
    )
    if missing_files:
        raise FileNotFoundError("Tabelas finais ausentes: " + ", ".join(missing_files))

    with duckdb.connect() as connection:
        for file_name in sorted(expected_files):
            file_path = output_dir / file_name
            if file_path.stat().st_size == 0:
                raise ValueError(f"Tabela final vazia: {file_path}")

            row = connection.execute(
                "SELECT COUNT(*) FROM read_parquet(?)", [str(file_path)]
            ).fetchone()
            if row is None or row[0] == 0:
                raise ValueError(f"Tabela final sem registros: {file_path}")

    logger.info(
        "Quality gate final aprovado: %s tabelas processadas", len(expected_files)
    )
