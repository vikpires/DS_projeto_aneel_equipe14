from src.config import SQL_DIR


# Lê um arquivo .sql do diretório de queries e preenche os parâmetros formatados
def load_sql_query(query_name: str, **params) -> str:

    file_path = SQL_DIR / f"{query_name}.sql"

    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo de query não encontrado: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        query_template = f.read()

    return query_template.format(**params)
