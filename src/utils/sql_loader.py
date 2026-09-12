import duckdb
import re
from src.config import SQL_DIR
from src.utils.csv_encoding import detect_csv_encoding


# Retorna o nome real da coluna no arquivo dentre uma lista de candidatas.
def resolve_column_name(
    con: duckdb.DuckDBPyConnection, file_path: str, candidates: list[str]
) -> str:
    if file_path.endswith(".parquet") or ".parquet" in file_path:
        cols_df = con.execute(
            f"DESCRIBE SELECT * FROM read_parquet('{file_path}') LIMIT 0;"
        ).fetchall()
    else:
        encoding = detect_csv_encoding(file_path)
        cols_df = con.execute(
            f"DESCRIBE SELECT * FROM read_csv_auto('{file_path}', encoding='{encoding}', all_varchar=true) LIMIT 0;"
        ).fetchall()

    actual_cols = [row[0] for row in cols_df]
    lookup = {re.sub(r"[^a-z0-9]", "", c.lower()): c for c in actual_cols}

    for candidate in candidates:
        normalized_candidate = re.sub(r"[^a-z0-9]", "", candidate.lower())
        if normalized_candidate in lookup:
            return lookup[normalized_candidate]

    raise ValueError(
        f"Nenhuma coluna compatível encontrada. "
        f"Esperadas: {candidates}; encontradas: {actual_cols}"
    )


# Lê um arquivo .sql do diretório de queries e preenche os parâmetros formatados
def load_sql_query(query_name: str, **params) -> str:

    file_path = SQL_DIR / f"{query_name}.sql"

    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo de query não encontrado: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        query_template = f.read()

    return query_template.format(**params)
