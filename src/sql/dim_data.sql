WITH range_datas AS (
    SELECT CAST(d AS DATE) AS data
    FROM generate_series(DATE '{ano_inicio}-01-01', DATE '{ano_fim}-12-31', INTERVAL 1 DAY) tbl(d)
)
SELECT 
    CAST(strftime(data, '%Y%m%d') AS INTEGER) AS DataKey,
    data AS Data,
    YEAR(data)::SMALLINT AS Ano,
    MONTH(data)::TINYINT AS MesNumero,
    CASE MONTH(data)
        WHEN 1 THEN 'Jan' WHEN 2 THEN 'Fev' WHEN 3 THEN 'Mar'
        WHEN 4 THEN 'Abr' WHEN 5 THEN 'Mai' WHEN 6 THEN 'Jun'
        WHEN 7 THEN 'Jul' WHEN 8 THEN 'Ago' WHEN 9 THEN 'Set'
        WHEN 10 THEN 'Out' WHEN 11 THEN 'Nov' WHEN 12 THEN 'Dez'
    END AS MesNome,
    strftime(data, '%Y-%m') AS AnoMes,
    'T' || CAST(QUARTER(data) AS VARCHAR) AS Trimestre
FROM range_datas
ORDER BY Data;