SELECT 1::TINYINT AS IndicadorKey, 'DEC' AS SigIndicador, 'Duração Equivalente de Interrupção por Unidade Consumidora' AS NomeIndicador, 'horas' AS Unidade
UNION ALL
SELECT 2::TINYINT AS IndicadorKey, 'FEC' AS SigIndicador, 'Frequência Equivalente de Interrupção por Unidade Consumidora' AS NomeIndicador, 'interrupções' AS Unidade;