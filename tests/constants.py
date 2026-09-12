# Constantes para simular URLs de download e nomes de arquivos durante os testes.
TEST_DOWNLOAD_URL = "https://example.test/data"
DATASET_FILENAME = "dataset.parquet"
OTHER_DATASET_FILENAME = "other.parquet"
DOWNLOAD_CHUNKS = (b"header", b"data")
DOWNLOAD_PAYLOAD = b"parquet"
NETWORK_ERROR_MESSAGE = "network failure"
RELEASE_ERROR_MESSAGE = "release unavailable"
PROCESSED_ARCHIVE_NAME = "fato_dimensao_2021_2025.zip"
QUERY_PROCESSED_FIXTURE = "SELECT 1 AS value"
PROCESSED_MANIFEST = '{"status": "SUCCESS"}'

# Queries de entrada para o teste de integração do modelo dimensional.
QUERY_FACT_DIM_CONTINUIDADE = """
SELECT 2021 AS AnoIndice, 5 AS NumPeriodoIndice,
       'AGENTE' AS SigAgente, '12345678000199' AS NumCNPJ,
       10 AS IdeConjunto, 'CONJUNTO' AS DscConjunto,
       'DEC' AS SigIndicador, 1.5 AS VlrIndiceEnviado
"""

QUERY_FACT_DIM_INTERRUPCOES = """
SELECT 2021 AS AnoIndice, 5 AS NumPeriodoIndice,
       TIMESTAMP '2021-05-10 10:00:00' AS DatInicioInterrupcao,
       TIMESTAMP '2021-05-10 11:30:00' AS DatFimInterrupcao,
       1.5 AS DuracaoHoras, 'AGENTE' AS SigAgente,
       '12345678000199' AS NumCNPJ, 10 AS IdeConjunto,
       '1' AS NumOrdemInterrupcao, 20 AS NumUnidadeConsumidora,
       100 AS NumConsumidorConjunto, 13.8 AS NumNivelTensao,
       'Programada' AS DscTipoInterrupcao,
       7 AS IdeMotivoInterrupcao,
       'Manutencao' AS DscFatoGeradorInterrupcao
"""

QUERY_FACT_DIM_LIMITES = """
SELECT '12345678000199' AS NumCNPJ, 10 AS IdeConjunto,
       'AGENTE' AS SigAgente, 'DEC' AS SigIndicador,
       2021 AS AnoIndice, 2.0 AS VlrLimite
"""

QUERY_FACT_DIM_ATRIBUTOS = """
SELECT '12345678000199' AS NumCNPJ, 10 AS IdeConjunto,
       'CONJUNTO' AS DscConjunto,
       DATE '2021-01-01' AS DatGeracaoConjuntoDados
"""

QUERY_FACT_DIM_REGIAO = """
SELECT 10 AS IdeConjunto, 1200401 AS CodMunicipio,
       'CRUZEIRO DO SUL' AS NomMunicipio, 'AC' AS SigUF,
       'NORTE' AS Regiao
"""

# Query de entrada para a base de Continuidade, simulando um registro de DEC.
QUERY_INPUT_CONTINUIDADE = """
SELECT 2021 AS AnoIndice, 1 AS NumPeriodoIndice, 'X' AS SigAgente,
    '12345678000199' AS NumCNPJ,
    10 AS IdeConjUndConsumidoras, 'Conjunto' AS DscConjUndConsumidoras,
       'DEC' AS SigIndicador, 1.5 AS VlrIndiceEnviado
"""

# Query de saída para a base de Continuidade, mapeando os campos de entrada para os nomes de coluna esperados.
QUERY_OUTPUT_CONTINUIDADE = """
SELECT *
FROM read_parquet('{raw_path}')
"""

# Query de entrada para a base de Interrupções, simulando um registro de interrupção.
QUERY_INPUT_INTERRUPCOES = """
SELECT 2021 AS NumAno,
       '2021-05-10 10:00:00' AS DatInicioInterrupcao,
       '2021-05-10 11:30:00' AS DatFimInterrupcao,
       ' X ' AS SigAgente,
    '12345678000199' AS NumCNPJ,
       20 AS IdeConjuntoUnidadeConsumidora,
    99 AS NumOrdemInterrupcao,
       15 AS NumUnidadeConsumidora,
       100 AS NumConsumidorConjunto,
       13.8 AS NumNivelTensao,
       'Programada' AS DscTipoInterrupcao,
       7 AS IdeMotivoInterrupcao,
       'Manutencao' AS DscFatoGeradorInterrupcao
"""

# Query de saída para a base de Interrupções, mapeando os campos de entrada para os nomes de coluna esperados.
QUERY_OUTPUT_INTERRUPCOES = """
SELECT AnoIndice, NumPeriodoIndice, DatInicioInterrupcao, DatFimInterrupcao,
       DuracaoHoras, SigAgente, NumCNPJ, IdeConjunto, NumOrdemInterrupcao,
       NumUnidadeConsumidora, NumConsumidorConjunto, NumNivelTensao,
       DscTipoInterrupcao, IdeMotivoInterrupcao, DscFatoGeradorInterrupcao
FROM read_parquet('{raw_path}')
"""

# Auditoria da base de Continuidade (DEC/FEC apurados por conjunto/mês)
QUERY_TEST_CONTINUIDADE = """
WITH metricas AS (
    SELECT 
        COUNT(*) AS total_linhas,
        COALESCE(MIN(AnoIndice), 0) AS min_ano,
        COALESCE(MAX(AnoIndice), 0) AS max_ano,
        
        -- Percentual de Nulos (escala 0 a 100)
        ROUND(COUNT(*) FILTER (WHERE IdeConjunto IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS pct_nulo_conjunto,
        ROUND(COUNT(*) FILTER (WHERE VlrIndiceEnviado IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS pct_nulo_indice,
        
        -- Valores Negativos
        COUNT(*) FILTER (WHERE VlrIndiceEnviado < 0) AS qtd_negativos
    FROM read_parquet('{raw_path}')
),
duplicatas AS (
    SELECT COUNT(*) AS qtd_duplicados
    FROM (
        SELECT IdeConjunto, AnoIndice, NumPeriodoIndice, SigIndicador
        FROM read_parquet('{raw_path}')
        GROUP BY IdeConjunto, AnoIndice, NumPeriodoIndice, SigIndicador
        HAVING COUNT(*) > 1
    )
)
SELECT 
    m.*, 
    d.qtd_duplicados 
FROM metricas m 
CROSS JOIN duplicatas d;
"""

# Auditoria da base consolidada de Interrupções (44M+ linhas)
QUERY_TEST_INTERRUPCOES = """
SELECT 
    COUNT(*) AS total_linhas,
    COALESCE(MIN(AnoIndice), 0) AS min_ano,
    COALESCE(MAX(AnoIndice), 0) AS max_ano,
    ROUND(COUNT(*) FILTER (WHERE IdeConjunto IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS dado_nulo_conjunto,
    ROUND(COUNT(*) FILTER (WHERE DatInicioInterrupcao IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS dado_nulo_data_inicio,
    ROUND(COUNT(*) FILTER (WHERE DuracaoHoras IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS dado_nulo_duracao,
    ROUND(COUNT(*) FILTER (WHERE NumConsumidorConjunto IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS dado_nulo_consumidores,
    
    -- Consistência Operacional e Regulatória
    COUNT(*) FILTER (WHERE DuracaoHoras < 0) AS qtd_duracao_negativa,
    COUNT(*) FILTER (WHERE DatFimInterrupcao < DatInicioInterrupcao) AS qtd_datas_invertidas,
    COUNT(*) FILTER (WHERE NumConsumidorConjunto < 0) AS qtd_consumidores_negativos
FROM read_parquet('{raw_path}');
"""
