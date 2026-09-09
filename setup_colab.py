import os
import subprocess
import sys
from pathlib import Path
from src.config import REPO_URL, REPO_NAME


# Função para configurar o ambiente no Google Colab
def setup():
    # 1. Verifica se já está dentro da pasta do repositório
    if Path.cwd().name != REPO_NAME:
        if not Path(REPO_NAME).exists():
            print(f"[1/3] Clonando repositório: {REPO_NAME}...")
            subprocess.run(["git", "clone", REPO_URL], check=True)
        else:
            print(f"[1/3] Pasta {REPO_NAME} já existe.")

        # Muda o diretório de trabalho de forma persistente
        os.chdir(REPO_NAME)
        print(f"Diretório alterado para: {Path.cwd()}")

    # 2. Instala dependências do requirements.txt
    req_file = Path("requirements.txt")
    if req_file.exists():
        print("[2/3] Instalando dependências...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-q", "-r", str(req_file)],
            check=True,
        )

    # 3. Adiciona src e raiz ao PYTHONPATH para imports funcionarem
    project_root = str(Path.cwd())
    src_dir = str(Path.cwd() / "src")

    for path in [project_root, src_dir]:
        if path not in sys.path:
            sys.path.insert(0, path)

    print("[3/3] Ambiente configurado com sucesso!")


if __name__ == "__main__":
    setup()
