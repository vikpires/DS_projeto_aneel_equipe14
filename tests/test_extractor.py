import pytest

from src.utils import download_utils
from tests.constants import (
    DATASET_FILENAME,
    DOWNLOAD_CHUNKS,
    NETWORK_ERROR_MESSAGE,
    TEST_DOWNLOAD_URL,
)


# Testa a função download_stream para garantir que ela promove o download corretamente e remove arquivos parciais.
def test_download_file_promotes_only_completed_file(
    monkeypatch, tmp_path, response_factory
):
    destination = tmp_path / "nested" / DATASET_FILENAME
    response = response_factory(DOWNLOAD_CHUNKS)
    monkeypatch.setattr(
        download_utils.requests,
        "get",
        lambda *args, **kwargs: response,
    )

    download_utils.download_stream(TEST_DOWNLOAD_URL, destination)

    assert destination.read_bytes() == b"".join(DOWNLOAD_CHUNKS)
    assert list(destination.parent.glob("*.part")) == []


# Testa a função download_stream para garantir que ela remove arquivos parciais e preserva o destino ausente em caso de falha.
def test_download_file_removes_partial_and_preserves_missing_destination(
    monkeypatch, tmp_path, response_factory
):
    destination = tmp_path / DATASET_FILENAME
    error = OSError(NETWORK_ERROR_MESSAGE)
    monkeypatch.setattr(
        download_utils.requests,
        "get",
        lambda *args, **kwargs: response_factory([], error=error),
    )

    with pytest.raises(OSError, match=NETWORK_ERROR_MESSAGE):
        download_utils.download_stream(TEST_DOWNLOAD_URL, destination)

    assert not destination.exists()
    assert list(tmp_path.glob("*.part")) == []


# Testa a função download_stream para garantir que o cache evita uma nova requisição.
def test_download_stream_skips_existing_destination(monkeypatch, tmp_path):
    destination = tmp_path / DATASET_FILENAME
    destination.write_bytes(b"already downloaded")

    def unexpected_request(*args, **kwargs):
        raise AssertionError("A rede não deve ser acessada para um arquivo existente")

    monkeypatch.setattr(download_utils.requests, "get", unexpected_request)

    download_utils.download_stream(TEST_DOWNLOAD_URL, destination)

    assert destination.read_bytes() == b"already downloaded"


# Testa a função download_stream para garantir que o cache é ignorado quando a opção force é True.
def test_download_stream_rejects_empty_response(
    monkeypatch, tmp_path, response_factory
):
    destination = tmp_path / DATASET_FILENAME
    response = response_factory([])
    monkeypatch.setattr(
        download_utils.requests,
        "get",
        lambda *args, **kwargs: response,
    )

    with pytest.raises(ValueError, match="Download vazio"):
        download_utils.download_stream(TEST_DOWNLOAD_URL, destination)

    assert not destination.exists()
    assert list(tmp_path.glob("*.part")) == []


# Testa a função download_stream para garantir que o cache é substituído quando o arquivo de destino está vazio.
def test_download_stream_replaces_empty_cache(monkeypatch, tmp_path, response_factory):
    destination = tmp_path / DATASET_FILENAME
    destination.touch()
    response = response_factory(DOWNLOAD_CHUNKS)
    monkeypatch.setattr(
        download_utils.requests,
        "get",
        lambda *args, **kwargs: response,
    )

    download_utils.download_stream(TEST_DOWNLOAD_URL, destination)

    assert destination.read_bytes() == b"".join(DOWNLOAD_CHUNKS)


# Testa a função download_stream para garantir que o cache é substituído quando o tamanho do arquivo de destino não corresponde ao cabeçalho Content-Length.
def test_download_stream_rejects_content_length_mismatch(
    monkeypatch, tmp_path, response_factory
):
    destination = tmp_path / DATASET_FILENAME
    response = response_factory(DOWNLOAD_CHUNKS, headers={"Content-Length": "999"})
    monkeypatch.setattr(
        download_utils.requests,
        "get",
        lambda *args, **kwargs: response,
    )

    with pytest.raises(ValueError, match="Tamanho inesperado"):
        download_utils.download_stream(TEST_DOWNLOAD_URL, destination)

    assert not destination.exists()
    assert list(tmp_path.glob("*.part")) == []
