WITH base AS (
    SELECT
        i.*,
        strip_accents(UPPER(TRIM(COALESCE(i.DscFatoGeradorInterrupcao, '')))) AS CausaOriginal,
        SPLIT_PART(REGEXP_REPLACE(strip_accents(UPPER(TRIM(COALESCE(i.DscFatoGeradorInterrupcao, '')))), '\s*[-;/]\s*', ';', 'g'), ';', 1) AS CausaParte1,
        SPLIT_PART(REGEXP_REPLACE(strip_accents(UPPER(TRIM(COALESCE(i.DscFatoGeradorInterrupcao, '')))), '\s*[-;/]\s*', ';', 'g'), ';', 2) AS CausaParte2,
        SPLIT_PART(REGEXP_REPLACE(strip_accents(UPPER(TRIM(COALESCE(i.DscFatoGeradorInterrupcao, '')))), '\s*[-;/]\s*', ';', 'g'), ';', 3) AS CausaParte3,
        SPLIT_PART(REGEXP_REPLACE(strip_accents(UPPER(TRIM(COALESCE(i.DscFatoGeradorInterrupcao, '')))), '\s*[-;/]\s*', ';', 'g'), ';', 4) AS CausaParte4
    FROM '{interrupcoes_path}' i
    WHERE i.AnoIndice = {ano}
), normalizada AS (
    SELECT
        base.*,
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
            WHEN REGEXP_REPLACE(CausaParte1, '^[^A-Z]*', '') LIKE 'EXTERNA%' THEN 'EXTERNA'
            WHEN REGEXP_REPLACE(CausaParte1, '^[^A-Z]*', '') LIKE 'INTERNA%' THEN 'INTERNA'
            WHEN REGEXP_MATCHES(CausaParte1, '^[A-Z]$') THEN 'OUTROS'
            ELSE COALESCE(
                NULLIF(UPPER(TRIM(REGEXP_REPLACE(CausaParte1, '\\s+', ' ', 'g'))), ''),
                'NAO INFORMADO'
            )
        END AS GrupoCausa,
        COALESCE(NULLIF(TRIM(CausaParte4), ''), NULLIF(TRIM(CausaParte3), ''),
                 NULLIF(TRIM(CausaParte2), ''), 'NAO INFORMADO') AS CausaDetalhada
    FROM base
), enriquecida AS (
    SELECT
        n.*,
        d.DistribuidoraKey,
        c.ConjuntoKey,
        c.DscConjunto,
        t.TipoInterrupcaoKey,
        t.TipoInterrupcao,
        m.MotivoInterrupcaoKey,
        m.MotivoCodigo,
        ca.CausaKey,
        (n.AnoIndice * 10000 + n.NumPeriodoIndice * 100 + 1)::INTEGER AS DataKey
    FROM normalizada n
    LEFT JOIN '{output_dir}/dim_distribuidora.parquet' d USING (NumCNPJ)
    LEFT JOIN '{output_dir}/dim_conjunto.parquet' c
        ON n.NumCNPJ = c.NumCNPJ AND n.IdeConjunto = c.IdeConjunto
    LEFT JOIN '{output_dir}/dim_tipo_interrupcao.parquet' t
        ON t.TipoInterrupcao = CASE
            WHEN UPPER(TRIM(COALESCE(n.DscTipoInterrupcao, ''))) LIKE '%NAO%PROGRAMAD%'
                OR UPPER(TRIM(COALESCE(n.DscTipoInterrupcao, ''))) LIKE '%NÃO%PROGRAMAD%'
                THEN 'NAO PROGRAMADA'
            WHEN UPPER(TRIM(COALESCE(n.DscTipoInterrupcao, ''))) LIKE '%PROGRAMAD%'
                THEN 'PROGRAMADA'
            ELSE 'NAO INFORMADO'
        END
    LEFT JOIN '{output_dir}/dim_motivo_interrupcao.parquet' m
        ON COALESCE(n.IdeMotivoInterrupcao, -1) = m.MotivoCodigo
    LEFT JOIN '{output_dir}/dim_causa_interrupcao.parquet' ca
        ON n.Origem = ca.Origem
       AND n.Programacao = ca.Programacao
       AND n.GrupoCausa = ca.GrupoCausa
       AND n.CausaDetalhada = ca.CausaDetalhada
), agregacao_mensal AS (
    SELECT
        DataKey,
        DistribuidoraKey,
        ConjuntoKey,
        TipoInterrupcaoKey,
        MotivoInterrupcaoKey,
        CausaKey,
        MODE(NumNivelTensao) AS NivelTensao,
        COUNT(*)::INTEGER AS QtdInterrupcoes,
        ROUND(SUM(COALESCE(DuracaoHoras, 0.0)), 4) AS DuracaoTotalHoras,
        ROUND(AVG(DuracaoHoras), 4) AS DuracaoMediaHoras,
        ROUND(MAX(DuracaoHoras), 4) AS MaiorInterrupcaoHoras,
        SUM(COALESCE(NumUnidadeConsumidora, 0))::BIGINT AS UnidadesAfetadasSoma,
        ROUND(SUM(COALESCE(NumUnidadeConsumidora, 0) * COALESCE(DuracaoHoras, 0.0)), 4) AS ConsumidorHoras,
        ROUND(SUM(CASE WHEN COALESCE(NumConsumidorConjunto, 0) > 0
            THEN (COALESCE(NumUnidadeConsumidora, 0) * COALESCE(DuracaoHoras, 0.0)) / NumConsumidorConjunto
            ELSE 0.0 END), 4) AS ContribDEC_Estimada,
        ROUND(SUM(CASE WHEN COALESCE(NumConsumidorConjunto, 0) > 0
            THEN CAST(COALESCE(NumUnidadeConsumidora, 0) AS DOUBLE) / NumConsumidorConjunto
            ELSE 0.0 END), 4) AS ContribFEC_Estimada
    FROM enriquecida
    GROUP BY 1, 2, 3, 4, 5, 6
)
SELECT
    (CAST('0x' || SUBSTR(MD5(
        CAST(DataKey AS VARCHAR) || '|' || CAST(DistribuidoraKey AS VARCHAR) || '|' ||
        CAST(ConjuntoKey AS VARCHAR) || '|' || CAST(TipoInterrupcaoKey AS VARCHAR) || '|' ||
        CAST(MotivoInterrupcaoKey AS VARCHAR) || '|' || CAST(CausaKey AS VARCHAR)
    ), 1, 16) AS UBIGINT) & 9223372036854775807) AS FatoCausaMensalKey,
    *
FROM agregacao_mensal;
