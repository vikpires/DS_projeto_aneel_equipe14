# Guia de Contribuição e Boas Práticas

Este documento orienta o fluxo de trabalho da equipe no repositório do projeto. Siga o passo a passo abaixo para garantir que todos trabalhem de forma sincronizada e sem conflitos de código.

---

## 1. Configuração Inicial do Ambiente

Escolha uma das abordagens abaixo de acordo com a sua preferência (Google Colab ou máquina local):

### Opção A: Execução via Google Colab

- Acesse o **Google Colab**.

- Selecione a aba `GitHub`, vincule sua conta e escolha o repositório do projeto.

- Abra o notebook desejado a partir da sua branch de trabalho (Branch padrão: `develop`).

- Para salvar alterações: vá em `Arquivo > Salvar uma cópia no GitHub...`, e insira a mensagem de commit.

- Se precisar importar módulos de `src/` ou rodar scripts completos, execute na primeira célula:

```bash
!git clone https://github.com/vikpires/ai_academy_final_challenge.git
%cd /content/ai_academy_final_challenge
!pip install -r requirements.txt
```

> [!WARNING]  
> Atenção no Colab: O armazenamento temporário é volátil. Sempre salve sua cópia no GitHub antes de fechar a aba do navegador. Nunca salve senhas, tokens ou credenciais nas células de código.

---

### Opção B: Configuração Local (VS Code / Terminal)

#### **1. Clonar o Repositório:**

```bash
git clone git@github.com:vikpires/ai_academy_final_challenge.git
cd ai_academy_final_challenge

```

#### **2. Criar e Ativar o Ambiente Virtual:**

- Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

- Linux / macOS::

```bash
cd ai_academy_final_challenge
python3 -m venv .venv
source .venv/bin/activate
```

#### **3. Instalar as Dependências:**

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 2. Fluxo de Trabalho com Git

> 📌 **Branch Principal de Trabalho:** Todo o desenvolvimento do projeto acontece a partir da branch **`develop`**, configurada como padrão. A branch `main` é restrita apenas para entregas finais avaliadas.

#### **1. Garantir que a branch `develop` está ativa e atualizada antes de iniciar qualquer alteração:**

```bash
git checkout develop      # Troca para a branch develop, caso esteja em outra
git fetch origin          # Busca novidades no GitHub sem aplicá-las ainda
git pull origin develop   # Baixa e sincroniza as atualizações mais recentes
```

> [!TIP]
> Se estiver no Google Colab, utilize o sinal de exclamação (!) antes de qualquer comando git. Ex.: `!git pull`

#### **2. Após realizar as alterações nos arquivos, salvar o progresso:**

```bash
git add . # Adiciona as alterações salvas no Stage
git commit -m ":sparkles: feat: descricao sucinta do que foi feito (#numero_da_issue)" # Salva as alterações realizadas


```

> [!NOTE]  
> Na aba Issues ou Project do GitHub, consulte o identificador numérico da task após o título (ex.: `Task 1.1 - Ingestão de Dados #2`). Inserir `#2` vincula automaticamente o commit ao card.

**Exemplos de Mensagens de Commits:**

:sparkles: feat: adiciona notebook de analise exploratoria (#6)

:recycle: refactor: adiciona notebook de analise exploratoria (#6)

:bug: fix: corrige tipagem da coluna de apuracao (#8)

:wrench: chore: atualiza dicionario de dados (#4)

:books: docs: adiciona o arquivo de README (#1)

> [!TIP]  
> Para saber mais, acesse o link sobre [padrões de commits](https://github.com/iuricode/padroes-de-commits).

#### **3. Envio do commit para o GitHub:**

```bash
git push origin develop
```

> [!CAUTION]
> Aviso importante: Evite editar um mesmo arquivo no qual outra pessoa esteja trabalhando simultaneamente para evitar conflitos de versão.

---

Essas são apenas algumas orientações gerais ao trabalhar com Git e GitHub. Demais dúvidas ou esclarecimentos, fiquem à vontade para perguntar.
