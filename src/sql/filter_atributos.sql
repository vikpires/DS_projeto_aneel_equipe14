WITH base_atributos AS (
    SELECT 
        LPAD(REGEXP_REPLACE(CAST({col_cnpj} AS VARCHAR), '\D', '', 'g'), 14, '0') AS NumCNPJ,
        CAST({col_conj} AS BIGINT) AS IdeConjunto,
        TRIM({col_desc}) AS DscConjunto,
        TRY_CAST(DatGeracaoConjuntoDados AS DATE) AS DatGeracaoConjuntoDados,
        * EXCLUDE({col_cnpj}, {col_conj}, {col_desc}, DatGeracaoConjuntoDados),
        ROW_NUMBER() OVER (
            PARTITION BY 
                LPAD(REGEXP_REPLACE(CAST({col_cnpj} AS VARCHAR), '\D', '', 'g'), 14, '0'),
                CAST({col_conj} AS BIGINT)
            ORDER BY TRY_CAST(DatGeracaoConjuntoDados AS DATE) DESC NULLS LAST
        ) AS rn
    FROM read_csv_auto('{raw_path}', encoding = '{csv_encoding}', all_varchar = true, ignore_errors = true)
    WHERE {col_conj} IS NOT NULL
)
SELECT * EXCLUDE(rn)
FROM base_atributos
WHERE rn = 1;