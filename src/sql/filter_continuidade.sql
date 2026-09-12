SELECT 
    CAST(AnoIndice AS INT) AS AnoIndice,
    CAST(NumPeriodoIndice AS INT) AS NumPeriodoIndice,
    TRIM(SigAgente) AS SigAgente,
    LPAD(REGEXP_REPLACE(CAST({col_cnpj} AS VARCHAR), '\D', '', 'g'), 14, '0') AS NumCNPJ,
    CAST({col_conj} AS BIGINT) AS IdeConjunto,
    UPPER(TRIM({col_desc})) AS DscConjunto,
    UPPER(TRIM(SigIndicador)) AS SigIndicador,
    ROUND(TRY_CAST(REPLACE(CAST(VlrIndiceEnviado AS VARCHAR), ',', '.') AS DOUBLE), 4) AS VlrIndiceEnviado
FROM read_parquet('{raw_path}')
WHERE CAST(AnoIndice AS INT) BETWEEN {ano_inicio} AND {ano_fim}
  AND UPPER(TRIM(SigIndicador)) IN ('DEC', 'FEC')
  AND NumPeriodoIndice BETWEEN 1 AND 12;