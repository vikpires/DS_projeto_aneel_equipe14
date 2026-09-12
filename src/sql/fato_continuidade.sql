WITH base AS (
    SELECT 
        c.AnoIndice,
        c.NumPeriodoIndice,
        c.NumCNPJ,
        c.IdeConjunto,
        c.SigIndicador,
        c.VlrIndiceEnviado AS VlrIndicador,
        l.VlrLimite
    FROM '{continuidade_path}' c
    LEFT JOIN '{limites_path}' l
        ON c.NumCNPJ = l.NumCNPJ 
       AND c.IdeConjunto = l.IdeConjunto 
       AND c.SigIndicador = l.SigIndicador 
       AND c.AnoIndice = l.AnoIndice
),
chaves AS (
    SELECT 
        (AnoIndice * 10000 + NumPeriodoIndice * 100 + 1)::INTEGER AS DataKey,
        d.DistribuidoraKey,
        j.ConjuntoKey,
        CASE WHEN SigIndicador = 'DEC' THEN 1 ELSE 2 END::TINYINT AS IndicadorKey,
        VlrIndicador,
        VlrLimite
    FROM base
    LEFT JOIN '{output_dir}/dim_distribuidora.parquet' d USING (NumCNPJ)
    LEFT JOIN '{output_dir}/dim_conjunto.parquet' j
        ON base.NumCNPJ = j.NumCNPJ AND base.IdeConjunto = j.IdeConjunto
)
SELECT 
    (CAST('0x' || SUBSTR(MD5(CAST(DataKey AS VARCHAR) || '|' || CAST(ConjuntoKey AS VARCHAR) || '|' || CAST(IndicadorKey AS VARCHAR)), 1, 16) AS UBIGINT) & 9223372036854775807) AS FatoContinuidadeKey,
    DataKey,
    DistribuidoraKey,
    ConjuntoKey,
    IndicadorKey,
    VlrIndicador,
    VlrLimite,
    CASE WHEN VlrIndicador IS NOT NULL AND VlrLimite IS NOT NULL AND VlrIndicador > VlrLimite THEN 1 ELSE 0 END::TINYINT AS UltrapassouLimite,
    GREATEST(COALESCE(VlrIndicador - VlrLimite, 0.0), 0.0) AS ExcessoSobreLimite,
    ROUND(VlrIndicador / NULLIF(VlrLimite, 0.0), 4) AS PercentualDoLimite
FROM chaves;