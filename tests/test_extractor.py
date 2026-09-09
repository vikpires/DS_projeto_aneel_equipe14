from importlib import import_module
import pytest

from tests.constants import (
    DATASET_FILENAME,
    DOWNLOAD_CHUNKS,
    DOWNLOAD_PAYLOAD,
    NETWORK_ERROR_MESSAGE,
    OTHER_DATASET_FILENAME,
    TEST_DOWNLOAD_URL,
    TEST_RELEASE_URL,
)

fetch_data = import_module("src.data.fetch_data")
download_stream = import_module("src.data.extractor")


# Testa a função download_stream para garantir que ela promove o download corretamente e remove arquivos parciais.
def test_download_file_promotes_only_completed_file(
    monkeypatch, tmp_path, response_factory
):
    destination = tmp_path / "nested" / DATASET_FILENAME
    response = response_factory(DOWNLOAD_CHUNKS)
    monkeypatch.setattr(
        download_stream.requests,
        "get",
        lambda *args, **kwargs: response,
    )

    download_stream.download_stream(TEST_DOWNLOAD_URL, destination)

    assert destination.read_bytes() == b"".join(DOWNLOAD_CHUNKS)
    assert list(destination.parent.glob("*.part")) == []


# Testa a função download_stream para garantir que ela remove arquivos parciais e preserva o destino ausente em caso de falha.
def test_download_file_removes_partial_and_preserves_missing_destination(
    monkeypatch, tmp_path, response_factory
):
    destination = tmp_path / DATASET_FILENAME
    error = OSError(NETWORK_ERROR_MESSAGE)
    monkeypatch.setattr(
        download_stream.requests,
        "get",
        lambda *args, **kwargs: response_factory([], error=error),
    )

    with pytest.raises(OSError, match=NETWORK_ERROR_MESSAGE):
        download_stream.download_stream(TEST_DOWNLOAD_URL, destination)

    assert not destination.exists()
    assert list(tmp_path.glob("*.part")) == []


# Testa a função fetch_data para garantir que ela promove o download corretamente e propaga falhas de forma adequada.
def test_fetch_data_promotes_download_and_propagates_failure(
    monkeypatch, tmp_path, successful_urlretrieve, failing_urlretrieve
):
    monkeypatch.setattr(fetch_data, "INTERIM_DIR", tmp_path)
    monkeypatch.setattr(fetch_data, "RELEASE_BASE_URL", TEST_RELEASE_URL)

    monkeypatch.setattr(
        fetch_data.urllib.request, "urlretrieve", successful_urlretrieve
    )
    fetch_data.fetch_data(files=[DATASET_FILENAME])

    assert (tmp_path / DATASET_FILENAME).read_bytes() == DOWNLOAD_PAYLOAD
    assert list(tmp_path.glob("*.part")) == []

    monkeypatch.setattr(fetch_data.urllib.request, "urlretrieve", failing_urlretrieve)
    with pytest.raises(RuntimeError, match=OTHER_DATASET_FILENAME):
        fetch_data.fetch_data(files=[OTHER_DATASET_FILENAME])

    assert not (tmp_path / OTHER_DATASET_FILENAME).exists()
    assert list(tmp_path.glob("*.part")) == []
