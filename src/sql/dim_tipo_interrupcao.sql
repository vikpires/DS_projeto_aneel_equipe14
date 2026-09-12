WITH tipos AS (
    SELECT DISTINCT
        CASE
            WHEN UPPER(TRIM(COALESCE(DscTipoInterrupcao, ''))) LIKE '%NAO%PROGRAMAD%'
                OR UPPER(TRIM(COALESCE(DscTipoInterrupcao, ''))) LIKE '%NÃO%PROGRAMAD%'
                THEN 'NAO PROGRAMADA'
            WHEN UPPER(TRIM(COALESCE(DscTipoInterrupcao, ''))) LIKE '%PROGRAMAD%'
                THEN 'PROGRAMADA'
            ELSE 'NAO INFORMADO'
        END AS TipoInterrupcao
    FROM '{interrupcoes_path}'
)
SELECT 
    CASE WHEN TipoInterrupcao = 'PROGRAMADA' THEN 2 ELSE 1 END::TINYINT AS TipoInterrupcaoKey,
    TipoInterrupcao
FROM tipos;