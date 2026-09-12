WITH dist_unicas AS (
    SELECT NumCNPJ, MAX(SigAgente) AS SigAgente
    FROM (
        SELECT NumCNPJ, SigAgente FROM '{continuidade_path}' WHERE NumCNPJ IS NOT NULL
        UNION ALL
        SELECT NumCNPJ, SigAgente FROM '{interrupcoes_path}' WHERE NumCNPJ IS NOT NULL
    ) fontes
    GROUP BY NumCNPJ
)
SELECT 
    -- Hash 63-bit BigInt positivo baseado no CNPJ
    SigAgente,
    NumCNPJ,
     ROW_NUMBER() OVER (ORDER BY NumCNPJ) AS DistribuidoraKey
FROM dist_unicas;