# Constantes para simular URLs de download e nomes de arquivos durante os testes.
TEST_DOWNLOAD_URL = "https://example.test/data"
TEST_RELEASE_URL = "https://example.test/release"
DATASET_FILENAME = "dataset.parquet"
OTHER_DATASET_FILENAME = "other.parquet"
DOWNLOAD_CHUNKS = (b"header", b"data")
DOWNLOAD_PAYLOAD = b"parquet"
NETWORK_ERROR_MESSAGE = "network failure"
RELEASE_ERROR_MESSAGE = "release unavailable"

# Query de entrada para a base de Continuidade, simulando um registro de DEC.
QUERY_INPUT_CONTINUIDADE = """
SELECT 2021 AS AnoIndice, 1 AS NumPeriodoIndice, 'X' AS SigAgente,
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
       20 AS IdeConjuntoUnidadeConsumidora,
       15 AS NumUnidadeConsumidora,
       100 AS NumConsumidorConjunto,
       13.8 AS NumNivelTensao,
       'Programada' AS DscTipoInterrupcao,
       7 AS IdeMotivoInterrupcao,
       'Manutencao' AS DscFatoGeradorInterrupcao
"""

# Query de saída para a base de Interrupções, mapeando os campos de entrada para os nomes de coluna esperados.
QUERY_OUTPUT_INTERRUPCOES = """
SELECT ano, mes, duracao_horas, sigla_distribuidora, id_conjunto,
       qtd_consumidores_afetados, qtd_consumidores_conjunto, nivel_tensao,
       tipo_interrupcao, id_motivo, fato_gerador
FROM read_parquet('{raw_path}')
"""

# Auditoria da base de Continuidade (DEC/FEC apurados por conjunto/mês)
QUERY_TEST_CONTINUIDADE = """
WITH metricas AS (
    SELECT 
        COUNT(*) AS total_linhas,
        COALESCE(MIN(ano), 0) AS min_ano,
        COALESCE(MAX(ano), 0) AS max_ano,
        
        -- Percentual de Nulos (escala 0 a 100)
        ROUND(COUNT(*) FILTER (WHERE id_conjunto IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS pct_nulo_conjunto,
        ROUND(COUNT(*) FILTER (WHERE dec_apurado IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS pct_nulo_dec,
        ROUND(COUNT(*) FILTER (WHERE fec_apurado IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS pct_nulo_fec,
        
        -- Valores Negativos
        COUNT(*) FILTER (WHERE dec_apurado < 0 OR fec_apurado < 0) AS qtd_negativos
    FROM read_parquet('{raw_path}')
),
duplicatas AS (
    SELECT COUNT(*) AS qtd_duplicados
    FROM (
        SELECT id_conjunto, ano, mes
        FROM read_parquet('{raw_path}')
        GROUP BY id_conjunto, ano, mes
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
    COALESCE(MIN(ano), 0) AS min_ano,
    COALESCE(MAX(ano), 0) AS max_ano,
    
    -- Percentual de Nulos (escala 0 a 100)
    ROUND(COUNT(*) FILTER (WHERE id_conjunto IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS dado_nulo_conjunto,
    ROUND(COUNT(*) FILTER (WHERE data_inicio IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS dado_nulo_data_inicio,
    ROUND(COUNT(*) FILTER (WHERE duracao_horas IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS dado_nulo_duracao,
    ROUND(COUNT(*) FILTER (WHERE qtd_consumidores_afetados IS NULL) * 100.0 / NULLIF(COUNT(*), 0), 4) AS dado_nulo_consumidores,
    
    -- Consistência Operacional e Regulatória
    COUNT(*) FILTER (WHERE duracao_horas < 0) AS qtd_duracao_negativa,
    COUNT(*) FILTER (WHERE data_fim < data_inicio) AS qtd_datas_invertidas,
    COUNT(*) FILTER (WHERE qtd_consumidores_afetados < 0) AS qtd_consumidores_negativos
FROM read_parquet('{raw_path}');
"""
