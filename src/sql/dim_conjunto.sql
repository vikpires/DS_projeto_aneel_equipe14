WITH base_conjuntos AS (
    SELECT DISTINCT NumCNPJ, IdeConjunto, DscConjunto FROM '{continuidade_path}' WHERE IdeConjunto IS NOT NULL
    UNION
    SELECT DISTINCT NumCNPJ, IdeConjunto, CAST(NULL AS VARCHAR) AS DscConjunto FROM '{interrupcoes_path}' WHERE IdeConjunto IS NOT NULL
),
consolidado AS (
    SELECT 
        NumCNPJ,
        IdeConjunto,
        COALESCE(MAX(DscConjunto), 'NÃO INFORMADO') AS DscConjunto
    FROM base_conjuntos
    GROUP BY NumCNPJ, IdeConjunto
), distribuidoras AS (
    SELECT
        NumCNPJ,
        ROW_NUMBER() OVER (ORDER BY NumCNPJ)::BIGINT AS DistribuidoraKey
    FROM (SELECT DISTINCT NumCNPJ FROM base_conjuntos) unicas
), numerado AS (
    SELECT
        ROW_NUMBER() OVER (ORDER BY c.NumCNPJ, c.IdeConjunto)::BIGINT AS ConjuntoKey,
        d.DistribuidoraKey,
        c.NumCNPJ,
        c.IdeConjunto,
        c.DscConjunto,
        COALESCE(CAST(r.CodMunicipio AS VARCHAR), 'NÃO INFORMADO') AS CodMunicipio,
        COALESCE(r.NomMunicipio, 'NÃO INFORMADO') AS NomMunicipio,
        COALESCE(r.SigUF, 'NÃO INFORMADO') AS SigUF,
        COALESCE(r.Regiao, 'NÃO INFORMADO') AS Regiao
    FROM consolidado c
    INNER JOIN distribuidoras d USING (NumCNPJ)
    LEFT JOIN '{regiao_path}' r
        ON c.IdeConjunto = r.IdeConjunto
)
SELECT
    ConjuntoKey,
    DistribuidoraKey,
    NumCNPJ,
    IdeConjunto,
    DscConjunto,
    CodMunicipio,
    NomMunicipio,
    SigUF,
    Regiao
FROM numerado;