import os
import subprocess
import sys
from pathlib import Path

REPO_NAME = "projeto_aneel_equipe14"
REPO_URL = "https://github.com/vikpires/projeto_aneel_equipe14.git"


def setup():
    # 1. Clona o repositório se ainda não estiver clonado
    if Path.cwd().name != REPO_NAME:
        if not Path(REPO_NAME).exists():
            print(f"[1/3] Clonando repositório: {REPO_NAME}...")
            subprocess.run(["git", "clone", REPO_URL], check=True)
        else:
            print(f"[1/3] Pasta {REPO_NAME} já existe.")

        # Altera o diretório de trabalho para dentro do projeto
        os.chdir(REPO_NAME)
        print(f"Diretório alterado para: {Path.cwd()}")

    # 2. Adiciona o repositório e 'src' ao sys.path para habilitar imports
    project_root = str(Path.cwd().resolve())
    src_dir = str((Path.cwd() / "src").resolve())

    for path in [project_root, src_dir]:
        if path not in sys.path:
            sys.path.insert(0, path)

    # 3. Instala dependências do requirements.txt
    req_file = Path("requirements.txt")
    if req_file.exists():
        print("[2/3] Instalando dependências...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-q", "-r", str(req_file)],
            check=True,
        )
    else:
        print("[2/3] Arquivo requirements.txt não encontrado, pulando instalação.")

    print("[3/3] Ambiente configurado com sucesso!")


if __name__ == "__main__":
    setup()
