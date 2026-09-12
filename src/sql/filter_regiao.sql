WITH regiao AS (
SELECT
	CAST({col_conj} AS BIGINT) AS IdeConjunto,
	TRY_CAST(CodMunicipio AS BIGINT) AS CodMunicipio,
	TRIM(NomMunicipio) AS Municipio,
	UPPER(TRIM(SigUF)) AS UF,
	CASE UPPER(TRIM(UF))
		WHEN 'AC' THEN 'NORTE' 
        WHEN 'AP' THEN 'NORTE'
		WHEN 'AM' THEN 'NORTE' 
        WHEN 'PA' THEN 'NORTE'
		WHEN 'RO' THEN 'NORTE' 
        WHEN 'RR' THEN 'NORTE'
		WHEN 'TO' THEN 'NORTE'
		WHEN 'AL' THEN 'NORDESTE' 
        WHEN 'BA' THEN 'NORDESTE'
		WHEN 'CE' THEN 'NORDESTE' 
        WHEN 'MA' THEN 'NORDESTE'
		WHEN 'PB' THEN 'NORDESTE' 
        WHEN 'PE' THEN 'NORDESTE'
		WHEN 'PI' THEN 'NORDESTE' 
        WHEN 'RN' THEN 'NORDESTE'
		WHEN 'SE' THEN 'NORDESTE'
		WHEN 'DF' THEN 'CENTRO-OESTE' 
        WHEN 'GO' THEN 'CENTRO-OESTE'
		WHEN 'MT' THEN 'CENTRO-OESTE' 
        WHEN 'MS' THEN 'CENTRO-OESTE'
		WHEN 'ES' THEN 'SUDESTE' 
        WHEN 'MG' THEN 'SUDESTE'
		WHEN 'RJ' THEN 'SUDESTE' 
        WHEN 'SP' THEN 'SUDESTE'
		WHEN 'PR' THEN 'SUL' 
        WHEN 'RS' THEN 'SUL' 
        WHEN 'SC' THEN 'SUL'
		ELSE 'NAO INFORMADO'
	END AS Regiao,
	ROW_NUMBER() OVER (
		PARTITION BY CAST({col_conj} AS BIGINT)
		ORDER BY TRY_CAST(CodMunicipio AS BIGINT), TRIM(Municipio)
	) AS rn
FROM read_csv_auto('{raw_path}', encoding = '{csv_encoding}', all_varchar = true, ignore_errors = true)
WHERE {col_conj} IS NOT NULL
)
SELECT IdeConjunto, CodMunicipio, Municipio, UF, Regiao
FROM regiao
WHERE rn = 1;

