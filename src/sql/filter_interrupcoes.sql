SELECT 
    -- Temporal
    CAST(NumAno AS INT) AS ano,
    CAST(EXTRACT(MONTH FROM CAST(DatInicioInterrupcao AS TIMESTAMP)) AS INT) AS mes,
    CAST(DatInicioInterrupcao AS TIMESTAMP) AS data_inicio,
    CAST(DatFimInterrupcao AS TIMESTAMP) AS data_fim,
    ROUND(
        date_diff('minute', CAST(DatInicioInterrupcao AS TIMESTAMP), CAST(DatFimInterrupcao AS TIMESTAMP)) / 60.0, 
        4
    ) AS duracao_horas,
    
    -- Distribuidora e Conjunto
    TRIM(SigAgente) AS sigla_distribuidora,
    CAST(IdeConjuntoUnidadeConsumidora AS BIGINT) AS id_conjunto,
    
    -- Métricas de Clientes Afetados
    CAST(NumUnidadeConsumidora AS BIGINT) AS qtd_consumidores_afetados,
    CAST(NumConsumidorConjunto AS BIGINT) AS qtd_consumidores_conjunto,
    
    -- Classificação e Causa Regulatórias
    CAST(NumNivelTensao AS DOUBLE) AS nivel_tensao,
    TRIM(DscTipoInterrupcao) AS tipo_interrupcao,
    CAST(IdeMotivoInterrupcao AS INT) AS id_motivo,
    TRIM(DscFatoGeradorInterrupcao) AS fato_gerador

FROM read_parquet('{raw_path}')
WHERE NumAno BETWEEN {ano_inicio} AND {ano_fim}