SELECT 
    -- Temporal
    CAST(AnoIndice AS INT) AS ano,
    CAST(NumPeriodoIndice AS INT) AS mes,

    -- Distribuidora e Conjunto
    TRIM(SigAgente) AS sigla_distribuidora,
    CAST(IdeConjUndConsumidoras AS BIGINT) AS id_conjunto,
    TRIM(DscConjUndConsumidoras) AS nome_conjunto,

    -- Indicadores de Continuidade 
    ROUND(
        MAX(TRY_CAST(REPLACE(CAST(VlrIndiceEnviado AS VARCHAR), ',', '.') AS DOUBLE)) 
        FILTER (WHERE UPPER(TRIM(SigIndicador)) = 'DEC'),
        4
    ) AS dec_apurado,

    ROUND(
        MAX(TRY_CAST(REPLACE(CAST(VlrIndiceEnviado AS VARCHAR), ',', '.') AS DOUBLE)) 
        FILTER (WHERE UPPER(TRIM(SigIndicador)) = 'FEC'),
        4
    ) AS fec_apurado

FROM read_parquet('{raw_path}')
WHERE AnoIndice BETWEEN {ano_inicio} AND {ano_fim}
GROUP BY 
    AnoIndice,
    NumPeriodoIndice,
    SigAgente,
    IdeConjUndConsumidoras,
    DscConjUndConsumidoras