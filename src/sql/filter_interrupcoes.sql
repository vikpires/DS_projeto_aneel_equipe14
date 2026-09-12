WITH base_raw AS (
    SELECT 
        CAST(NumAno AS INT) AS AnoIndice,
        CAST(EXTRACT(MONTH FROM TRY_CAST(DatInicioInterrupcao AS TIMESTAMP)) AS INT) AS NumPeriodoIndice,
        TRY_CAST(DatInicioInterrupcao AS TIMESTAMP) AS DatInicioInterrupcao,
        TRY_CAST(DatFimInterrupcao AS TIMESTAMP) AS DatFimInterrupcao,
        ROUND(
            date_diff('minute', TRY_CAST(DatInicioInterrupcao AS TIMESTAMP), TRY_CAST(DatFimInterrupcao AS TIMESTAMP)) / 60.0, 
            4
        ) AS DuracaoHoras,
        TRIM(SigAgente) AS SigAgente,
        LPAD(REGEXP_REPLACE(CAST({col_cnpj} AS VARCHAR), '\D', '', 'g'), 14, '0') AS cnpj_formatado,
        CAST({col_conj} AS BIGINT) AS IdeConjunto,
        TRIM(COALESCE(CAST({col_ordem} AS VARCHAR), '')) AS NumOrdemInterrupcao,
        TRY_CAST(NumUnidadeConsumidora AS BIGINT) AS NumUnidadeConsumidora,
        TRY_CAST(NumConsumidorConjunto AS BIGINT) AS NumConsumidorConjunto,
        TRY_CAST(NumNivelTensao AS DOUBLE) AS NumNivelTensao,
        TRIM(COALESCE(DscTipoInterrupcao, 'NAO INFORMADO')) AS DscTipoInterrupcao,
        TRY_CAST({col_motivo} AS INT) AS IdeMotivoInterrupcao,
        TRIM(COALESCE({col_fato}, 'NAO INFORMADO')) AS DscFatoGeradorInterrupcao
    FROM read_parquet('{raw_path}')
    WHERE CAST(NumAno AS INT) BETWEEN {ano_inicio} AND {ano_fim}
)
SELECT 
    AnoIndice,
    NumPeriodoIndice,
    DatInicioInterrupcao,
    DatFimInterrupcao,
    DuracaoHoras,
    SigAgente,
    cnpj_formatado AS NumCNPJ,
    IdeConjunto,
    NumOrdemInterrupcao,
    NumUnidadeConsumidora,
    NumConsumidorConjunto,
    NumNivelTensao,
    DscTipoInterrupcao,
    IdeMotivoInterrupcao,
    DscFatoGeradorInterrupcao
FROM base_raw;