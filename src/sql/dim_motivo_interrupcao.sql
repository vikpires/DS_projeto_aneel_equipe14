WITH motivos(MotivoCodigo, MotivoDescricao) AS (
    VALUES 
        (0, 'Não houve expurgo'),
        (1, 'Falha nas instalações da unidade consumidora sem afetar terceiros'),
        (2, 'Obra de interesse exclusivo do consumidor'),
        (3, 'Situação de emergência'),
        (4, 'Suspensão por inadimplemento ou deficiência técnica/segurança da UC'),
        (5, 'Programa de racionamento instituído pela União'),
        (6, 'Ocorrência em dia crítico'),
        (7, 'Esquema de alívio de carga solicitado pelo ONS'),
        (8, 'Origem externa ao sistema de distribuição')
)
SELECT 
    MotivoCodigo::INTEGER AS MotivoInterrupcaoKey,
    MotivoCodigo,
    MotivoDescricao,
    CASE WHEN MotivoCodigo = 0 THEN 0 ELSE 1 END::TINYINT AS EhExpurgada
FROM motivos;