import pytest
import duckdb

from tests.constants import DOWNLOAD_PAYLOAD, RELEASE_ERROR_MESSAGE


# Classe FakeResponse para simular respostas de requisições HTTP durante os testes
class FakeResponse:
    def __init__(self, chunks, error=None):
        self.chunks = chunks
        self.error = error

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def raise_for_status(self):
        if self.error:
            raise self.error

    def iter_content(self, chunk_size):
        return iter(self.chunks)


# Fornece a classe FakeResponse durante os testes
@pytest.fixture
def response_factory():
    return FakeResponse


# Simula o comportamento de urllib.request.urlretrieve durante os testes
@pytest.fixture
def successful_urlretrieve():
    def write_download(url, destination):
        destination.write_bytes(DOWNLOAD_PAYLOAD)

    return write_download


# Simula falha no download, escrevendo um arquivo parcial antes de lançar uma exceção.
@pytest.fixture
def failing_urlretrieve():
    def fail_download(url, destination):
        destination.write_bytes(b"partial")
        raise OSError(RELEASE_ERROR_MESSAGE)

    return fail_download


# Cria e gerencia a conexão com o DuckDB durante a sessão de testes
@pytest.fixture(scope="session")
def db_connection():
    con = duckdb.connect()
    yield con
    con.close()
