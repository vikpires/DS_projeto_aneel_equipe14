WITH base_limites AS (
    SELECT 
        LPAD(REGEXP_REPLACE(CAST({col_cnpj} AS VARCHAR), '\D', '', 'g'), 14, '0') AS NumCNPJ,
        CAST({col_conj} AS BIGINT) AS IdeConjunto,
        TRIM(SigAgente) AS SigAgente,
        UPPER(TRIM(SigIndicador)) AS SigIndicador,
        CAST(AnoLimiteQualidade AS INT) AS AnoIndice,
        ROUND(TRY_CAST(REPLACE(CAST(VlrLimite AS VARCHAR), ',', '.') AS DOUBLE), 4) AS VlrLimite,
        ROW_NUMBER() OVER (
            PARTITION BY 
                LPAD(REGEXP_REPLACE(CAST({col_cnpj} AS VARCHAR), '\D', '', 'g'), 14, '0'),
                CAST({col_conj} AS BIGINT),
                UPPER(TRIM(SigIndicador)),
                CAST(AnoLimiteQualidade AS INT)
            ORDER BY 1
        ) AS rn
    FROM read_csv_auto('{raw_path}', encoding = '{csv_encoding}', all_varchar = true, ignore_errors = true)
    WHERE CAST(AnoLimiteQualidade AS INT) BETWEEN {ano_inicio} AND {ano_fim}
      AND UPPER(TRIM(SigIndicador)) IN ('DEC', 'FEC')
)
SELECT 
    NumCNPJ,
    IdeConjunto,
    SigAgente,
    SigIndicador,
    AnoIndice,
    VlrLimite
FROM base_limites
WHERE rn = 1;