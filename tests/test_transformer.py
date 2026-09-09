from importlib import import_module
import pytest

fetch_data = import_module("src.data.fetch_data")
from src.data.transformer import transform_data
from src.config import ANO_INICIO, ANO_FIM
from tests.constants import (
    QUERY_INPUT_CONTINUIDADE,
    QUERY_INPUT_INTERRUPCOES,
    QUERY_OUTPUT_CONTINUIDADE,
    QUERY_OUTPUT_INTERRUPCOES,
)


# Executa a transformação de dados e verifica se o arquivo Parquet de Continuidade contém os dados esperados.
def test_execute_continuidade_transformation_creates_expected_parquet(
    tmp_path, db_connection
):
    raw_path = tmp_path / "raw.parquet"
    output_path = tmp_path / "output.parquet"
    db_connection.sql(QUERY_INPUT_CONTINUIDADE).write_parquet(str(raw_path))
    transform_data(
        db_connection,
        "filter_continuidade",
        raw_path,
        output_path,
        ano_inicio=ANO_INICIO,
        ano_fim=ANO_FIM,
    )

    result = db_connection.sql(
        QUERY_OUTPUT_CONTINUIDADE.format(raw_path=output_path)
    ).fetchall()
    assert result == [(2021, 1, "X", 10, "Conjunto", 1.5, None)]


# Executa a transformação de dados e verifica se o arquivo Parquet de interrupções contém os dados esperados.
def test_execute_interrupcoes_transformation_creates_expected_parquet(
    tmp_path, db_connection
):
    raw_path = tmp_path / "raw_interrupcoes.parquet"
    output_path = tmp_path / "output_interrupcoes.parquet"
    db_connection.sql(QUERY_INPUT_INTERRUPCOES).write_parquet(str(raw_path))

    transform_data(
        db_connection,
        "filter_interrupcoes",
        raw_path,
        output_path,
        ano_inicio=ANO_INICIO,
        ano_fim=ANO_FIM,
    )

    result = db_connection.sql(
        QUERY_OUTPUT_INTERRUPCOES.format(raw_path=output_path)
    ).fetchall()
    assert result == [
        (
            2021,
            5,
            1.5,
            "X",
            20,
            15,
            100,
            13.8,
            "Programada",
            7,
            "Manutencao",
        )
    ]


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])
