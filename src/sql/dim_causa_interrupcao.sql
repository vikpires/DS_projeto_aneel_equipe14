WITH causas_unicas AS (
    SELECT DISTINCT
        strip_accents(UPPER(TRIM(COALESCE(DscFatoGeradorInterrupcao, '')))) AS CausaOriginal
    FROM '{interrupcoes_path}'
), partes AS (
    SELECT
        CausaOriginal,
        SPLIT_PART(REGEXP_REPLACE(CausaOriginal, '\s*[-;/]\s*', ';', 'g'), ';', 1) AS Parte1,
        SPLIT_PART(REGEXP_REPLACE(CausaOriginal, '\s*[-;/]\s*', ';', 'g'), ';', 2) AS Parte2,
        SPLIT_PART(REGEXP_REPLACE(CausaOriginal, '\s*[-;/]\s*', ';', 'g'), ';', 3) AS Parte3,
        SPLIT_PART(REGEXP_REPLACE(CausaOriginal, '\s*[-;/]\s*', ';', 'g'), ';', 4) AS Parte4
    FROM causas_unicas
), padronizadas AS (
    SELECT
        CASE
            WHEN CausaOriginal = '' THEN 'NAO INFORMADO'
            WHEN CausaOriginal LIKE '%EXTERNA%' THEN 'EXTERNA'
            WHEN CausaOriginal LIKE '%INTERNA%'
                OR CausaOriginal LIKE '%PROPRIA%'
                OR CausaOriginal LIKE '%PRÓPRIA%' THEN 'INTERNA'
            ELSE 'NAO INFORMADO'
        END AS Origem,
        CASE
            WHEN CausaOriginal LIKE '%NAO PROGRAMAD%'
                OR CausaOriginal LIKE '%NÃO PROGRAMAD%' THEN 'NAO PROGRAMADA'
            WHEN CausaOriginal LIKE '%PROGRAMAD%' THEN 'PROGRAMADA'
            ELSE 'NAO INFORMADO'
        END AS Programacao,
        CASE
            WHEN REGEXP_REPLACE(Parte1, '^[^A-Z]*', '') LIKE '%EXTERNA%' THEN 'EXTERNA'
            WHEN REGEXP_REPLACE(Parte1, '^[^A-Z]*', '') LIKE '%INTERNA%' THEN 'INTERNA'
            WHEN REGEXP_MATCHES(Parte1, '^[A-Z]$') THEN 'OUTROS'
            ELSE COALESCE(
                NULLIF(UPPER(TRIM(REGEXP_REPLACE(Parte1, '\\s+', ' ', 'g'))), ''),
                'NAO INFORMADO'
            )
        END AS GrupoCausa,
        COALESCE(NULLIF(TRIM(Parte4), ''), NULLIF(TRIM(Parte3), ''),
                 NULLIF(TRIM(Parte2), ''), 'NAO INFORMADO') AS CausaDetalhada
    FROM partes
), distintas AS (
    SELECT DISTINCT Origem, Programacao, GrupoCausa, CausaDetalhada
    FROM padronizadas
)
SELECT
    ROW_NUMBER() OVER (ORDER BY Origem, Programacao, GrupoCausa, CausaDetalhada)::BIGINT AS CausaKey,
    Origem,
    Programacao,
    GrupoCausa,
    CausaDetalhada
FROM distintas;