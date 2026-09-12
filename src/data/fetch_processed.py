import logging
from typing import Sequence

from src.config import PROCESSED_DIR, PROCESSED_RELEASE_FILES, RELEASE_BASE_URL
from src.utils.download_utils import download_and_extract

logger = logging.getLogger(__name__)


# Baixa e extrai as tabelas fato e dimensão da release v0.1.0.
def fetch_processed(
    files: Sequence[str] = PROCESSED_RELEASE_FILES,
    force: bool = False,
) -> None:
    for file_name in files:
        download_and_extract(RELEASE_BASE_URL, file_name, PROCESSED_DIR, force)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    fetch_processed()
