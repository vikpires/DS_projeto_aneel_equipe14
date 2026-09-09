import pytest


# Executa a suíte de testes para validar o pipeline de ingesstão, processamento e qualidade dos dados.
def run_validation() -> None:
    retcode = pytest.main(
        [
            "-v",
            "tests/test_extractor.py",
            "tests/test_transformer.py",
            "tests/test_data_quality.py",
        ]
    )
    if retcode != pytest.ExitCode.OK:
        raise RuntimeError(f"Validação de dados falhou! Código de erro: {retcode}")


print("[SUCESSO] Todos os testes passaram com sucesso!")
