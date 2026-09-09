from pathlib import Path
import pytest
from src.config import ANO_INICIO, ANO_FIM, CONT_PATH, INT_PATH
from tests.constants import QUERY_TEST_CONTINUIDADE, QUERY_TEST_INTERRUPCOES


# Validações da base de indicadores de continuidade de fornecimento de energia elétrica
class TestContinuidade:

    def test_existent_file(self):
        assert Path(CONT_PATH).exists(), f"Arquivo não encontrado: {CONT_PATH}"

    def test_quality_rules(self, db_connection):
        query = QUERY_TEST_CONTINUIDADE.format(raw_path=CONT_PATH)
        df_result = db_connection.execute(query).df()
        row = df_result.iloc[0]

        # Janela Temporal Estrita (2021-2025)
        assert row["total_linhas"] > 0, "Dataset de continuidade vazio."
        assert (
            row["min_ano"] >= ANO_INICIO
        ), f"Ano mínimo {row['min_ano']} fora do escopo."
        assert row["max_ano"] <= ANO_FIM, f"Ano máximo {row['max_ano']} fora do escopo."

        # Taxa de Nulos (<1%)
        assert (
            row["pct_nulo_conjunto"] <= 1.0
        ), f"Nulo Conjunto ({row['pct_nulo_conjunto']}%) > 1%"
        assert row["pct_nulo_dec"] <= 1.0, f"Nulo DEC ({row['pct_nulo_dec']}%) > 1%"
        assert row["pct_nulo_fec"] <= 1.0, f"Nulo FEC ({row['pct_nulo_fec']}%) > 1%"

        # Integridade Relacional e Numérica
        assert (
            row["qtd_duplicados"] == 0
        ), f"Encontradas {row['qtd_duplicados']} chaves duplicadas (id_conjunto, ano, mes)."
        assert (
            row["qtd_negativos"] == 0
        ), f"Encontrados {row['qtd_negativos']} valores negativos em DEC/FEC apurados."


# Validações da base de indicadores de interrupções de fornecimento de energia elétrica
class TestInterrupcoes:

    def test_existent_file(self):
        assert Path(INT_PATH).exists(), f"Arquivo não encontrado: {INT_PATH}"

    def test_quality_rules(self, db_connection):
        query = QUERY_TEST_INTERRUPCOES.format(raw_path=INT_PATH)
        df_result = db_connection.execute(query).df()
        row = df_result.iloc[0]

        # Janela Temporal Estrita (2021-2025)
        assert row["total_linhas"] > 0, "Dataset de interrupções vazio."
        assert (
            row["min_ano"] >= ANO_INICIO
        ), f"Ano mínimo {row['min_ano']} fora do escopo."
        assert row["max_ano"] <= ANO_FIM, f"Ano máximo {row['max_ano']} fora do escopo."

        # Taxa de Nulos (< 1%)
        assert (
            row["dado_nulo_conjunto"] <= 1.0
        ), f"Nulo Conjunto ({row['dado_nulo_conjunto']}%) > 1%"
        assert (
            row["dado_nulo_data_inicio"] <= 1.0
        ), f"Nulo Data Início ({row['dado_nulo_data_inicio']}%) > 1%"
        assert (
            row["dado_nulo_duracao"] <= 1.0
        ), f"Nulo Duração ({row['dado_nulo_duracao']}%) > 1%"
        assert (
            row["dado_nulo_consumidores"] <= 1.0
        ), f"Nulo Consumidores Afetados ({row['dado_nulo_consumidores']}%) > 1%"

        # Consistência Operacional e Cronológica
        assert (
            row["qtd_duracao_negativa"] == 0
        ), f"Encontradas {row['qtd_duracao_negativa']} durações negativas."
        assert (
            row["qtd_datas_invertidas"] == 0
        ), f"Encontradas {row['qtd_datas_invertidas']} datas de início/fim invertidas."
        assert (
            row["qtd_consumidores_negativos"] == 0
        ), f"Encontrados {row['qtd_consumidores_negativos']} consumidores afetados com valor negativo."


if __name__ == "__main__":
    import pytest

    pytest.main([__file__, "-v"])
