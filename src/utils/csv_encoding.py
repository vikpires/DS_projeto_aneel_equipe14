from pathlib import Path


# Detecta a codificação dos CSVs antes da leitura pelo DuckDB.
def detect_csv_encoding(file_path: str | Path) -> str:
    content = Path(file_path).read_bytes()
    for encoding in ("utf-8", "cp1252"):
        try:
            content.decode(encoding)
            return encoding
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(
        "csv", content, 0, len(content), f"Codificação CSV não suportada: {file_path}"
    )
