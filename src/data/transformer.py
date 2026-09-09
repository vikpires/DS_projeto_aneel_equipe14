import duckdb
from pathlib import Path
from src.config import ANO_FIM, ANO_INICIO, INTERIM_DIR
from src.data.constants import DATASETS
from src.utils.sql_loader import load_sql_query


# Carrega a query externa e executa a transformação no DuckDB.
def transform_data(
    con: duckdb.DuckDBPyConnection,
    query_name: str,
    raw_path: Path | str,
    out_path: Path | str,
    **kwargs,
):

    # Converte para strings limpas no formato POSIX
    raw_str = raw_path.as_posix() if isinstance(raw_path, Path) else str(raw_path)
    out_str = out_path.as_posix() if isinstance(out_path, Path) else str(out_path)
    out_name = Path(out_str).name

    print(f"[DUCKDB] Processando pipeline via '{query_name}.sql' -> {out_name}...")

    sql_query = load_sql_query(query_name=query_name, raw_path=raw_str, **kwargs)

    con.execute(f"""
        COPY ({sql_query})
        TO '{out_str}'
        (FORMAT PARQUET, COMPRESSION 'SNAPPY')
    """)

    print(f"[SUCESSO] Gerado: {out_name}")


# Executar o processo de transformação de dados.
def run_transform_data():
    with duckdb.connect() as con:
        print("\n--- Processando Continuidade via DuckDB ---")
        transform_data(
            con=con,
            query_name=DATASETS["continuidade"]["query_name"],
            raw_path=DATASETS["continuidade"]["raw_path"],
            out_path=DATASETS["continuidade"]["out_path"],
            ano_inicio=ANO_INICIO,
            ano_fim=ANO_FIM,
        )

        print("\n--- Processando Interrupções (Consolidando Lote) via DuckDB ---")
        transform_data(
            con=con,
            query_name=DATASETS["interrupcoes"]["query_name"],
            raw_path=DATASETS["interrupcoes"]["raw_pattern"],
            out_path=DATASETS["interrupcoes"]["out_path"],
            ano_inicio=ANO_INICIO,
            ano_fim=ANO_FIM,
        )

    print(f"\nProcessamento concluído! Verifique a pasta {INTERIM_DIR}.")
