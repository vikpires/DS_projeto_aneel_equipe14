 <div align="center">
   <img src=".\docs\assets\energy_towers.jpg" width=100% alt="Imagem de torres de energia elétrica" /> 
 </div>

# Projeto ANEEL - Energia em Risco
### Análise de Dados de Continuidade Elétrica e Previsão de Risco Regulatório (ANEEL)

<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/DuckDB-FFF000?style=for-the-badge&logo=duckdb&logoColor=black" alt="DuckDB" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge" alt="Seaborn" />  
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI" />
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git" />

</p>

---

## Descrição

Projeto de **Análise de Dados e Machine Learning** desenvolvido sobre dados públicos da Agência Nacional de Energia Elétrica (ANEEL), com foco no diagnóstico dos indicadores de continuidade do fornecimento elétrico (DEC e FEC) e na mitigação de riscos e compensações regulatórias no Brasil. Trabalho desenvolvido como projeto prático da formação **AI Talent Academy**, da _White Cube_.

---

## Sumário

- [1. Contexto](#1-contexto)
- [2. Objetivo Geral](#2-objetivo-geral)
- [3. Objetivos Específicos](#3-objetivos-específicos)
- [4. Base de Dados](#4-base-de-dados)
- [5. Metodologia](#5-metodologia)
- [6. Cronograma e Fases](#6-cronograma-e-fases)
- [7. Organização dos Diretorios](#7-organização-dos-diretórios)
- [8. Equipe](#8-equipe)

---

## 1. Contexto

No setor de distribuição de energia elétrica no Brasil, a **Agência Nacional de Energia Elétrica (ANEEL)** estabelece metas e padrões contratuais estritos de qualidade por meio de dois indicadores coletivos de continuidade:

- **DEC (Duração Equivalente de Interrupção por Unidade Consumidora):** Mede o tempo médio (em horas) que os consumidores atendidos por determinado conjunto ficaram sem energia.

- **FEC (Frequência Equivalente de Interrupção por Unidade Consumidora):** Mede a quantidade média de vezes em que ocorreram interrupções no fornecimento.

A transgressão desses limites regulatórios acarreta compensações financeiras obrigatórias repassadas diretamente na fatura dos consumidores afetados, impactando a receita operacional líquida das concessionárias e sua reputação institucional.

---

## 2. Objetivo Geral

Construir uma solução integrada de Análise de Dados e Machine Learning que permita analisar o comportamento histórico dos indicadores DEC e FEC, diagnosticar reincidências de transgressões e estimar a probabilidade de descumprimento dos limites regulatórios futuros em nível de conjunto consumidor.

---

## 3. Objetivos Específicos

* Consolidar a série histórica (2023–2025) dos dados de continuidade da ANEEL

* Comparar os valores apurados com os limites regulatórios, mapeando taxas de transgressão e gerando ranking dos conjuntos elétricos mais críticos.

* Identificar comportamentos cíclicos e disparidades regionais no desempenho operacional.

* Treinar e avaliar um modelo de Machine Learning supervisionado para classificar o risco de violação (Apurado > Limite) de conjuntos elétricos no horizonte mensal subsequente.

* Disponibilizar os diagnósticos, estimativas de passivo financeiro e scores de risco preditivo em dashboards interativos no Power BI sob modelagem *Star Schema*.

---

## 4. Base de Dados

Os dados utilizados são públicos e extraídos do portal de dados abertos da ANEEL. Para fins de análise, o conjunto de dados será limitado a um período de 3 anos (2023-2026):

**Datasets:** 
- [Indicadores Coletivos de Continuidade (DEC e FEC)](https://dadosabertos.aneel.gov.br/pt_BR/dataset/indicadores-coletivos-de-continuidade-dec-e-fec)
- [Interrupções de Energia Elétrica nas Redes de Distribuição)](https://dadosabertos.aneel.gov.br/pt_BR/dataset/indicadores-coletivos-de-continuidade-dec-e-fec)

**Métricas Principais:** 
- Valores apurados, limites regulatórios mensais e anuais contratados.

---

## 5. Metodologia

O projeto adotará o framework **CRISP-DM**, estruturado em seis fases:

1. **Compreensão do Negócio (Business Understanding):** Mapeamento das regras regulatórias (PRODIST/ANEEL), impacto financeiro das compensações por violação de DEC/FEC, definição de KPIs de negócio, métricas técnicas e escopo do projeto.

2. **Compreensão dos Dados (Data Understanding):** Ingestão das bases anuais, auditoria de integridade e Análise Exploratória de Dados (EDA).

3. **Preparação dos Dados (Data Preparation):** Limpeza, padronização e estruturação do modelo dimensional.

4. **Modelagem (Modeling):** Desenvolvimento da camada analítica de medidas em DAX e modelagem preditiva de risco regulatório.

5. **Avaliação (Evaluation):** Auditoria das regras de agregação e validação de desempenho dos modelos.

6. **Implantação (Deployment) & Demo Day:** Desenvolvimento do relatório executivo no Power BI, documentação técnica e apresentação final.

---

## 6. Cronograma e Fases

<p align="left">
  <a href="https://github.com/users/vikpires/projects/7/views/4?sliceBy[columnId]=Milestone">
    <img src="https://img.shields.io/badge/Backlog_&_Roadmap-1074e7?style=for-the-badge&logo=github&logoColor=white" alt="Backlog e Roadmap" />
  </a>
</p>

| Fase / Marco | Status | Período | Tarefas |
| :--- | :---: | :---: | :---: |
| **01:  Compreensão do Negócio (Business Understanding)** | Concluído | Semana 4 | [Ver Tarefas](https://github.com/vikpires/DS_projeto_aneel_equipe14/milestone/1) |
| **02: Compreensão dos Dados (Data Understanding)** | Em Progresso | Semana 5 | [Ver Tarefas](https://github.com/vikpires/DS_projeto_aneel_equipe14/milestone/6) |
| **03: Preparação dos Dados (Data Preparation)** | A Iniciar | Semana 6 | [Ver Tarefas](https://github.com/vikpires/DS_projeto_aneel_equipe14/milestone/2) |
| **04: Modelagem (Modeling)** | A Iniciar | Semana 7 | [Ver Tarefas](https://github.com/vikpires/DS_projeto_aneel_equipe14/milestone/3) |
| **05: Avaliação (Evaluation)** | A Iniciar | Semana 8 | [Ver Tarefas](https://github.com/vikpires/DS_projeto_aneel_equipe14/milestone/4) |
| **06: Implantação (Deployment) & Demo Day** | A Iniciar | Semana 8 | [Ver Tarefas](https://github.com/vikpires/DS_projeto_aneel_equipe14/milestone/5) |

---

## 7. Organização dos Diretórios

```markdown
├── 📁 data/
│   ├── 📁 raw/            # Dados brutos originais (Camada Bronze)
│   ├── 📁 interim/        # Dados intermediários (Camada Silver)
│   ├── 📁 external/       # Dados externos e bases de apoio
│   └── 📁 processed/      # Dados finais tratados para análise e modelagem (Camada Gold)
│
├── 📁 docs/               # Documentação do projeto, escopo e dicionário de dados
│    ├── 📁 assets/        # Imagens e diagramas para documentação
│
├── 📁 models/             # Artefatos e arquivos de modelos treinados
├── 📁 notebooks/          # Notebooks de exploração e prototipagem
├── 📁 pbix/               # Arquivos e templates do Power BI
├── 📁 reports/            # Relatórios e apresentações
├── 📁 references/         # Manuais, guias metodológicos e materiais de consulta
├── 📁 src/                # Código-fonte modular e scripts do projeto
├── 📄 gitignore           # Regras de arquivos ignorados pelo Git
├── 📄 LICENSE             # Licença de uso e distribuição do projeto
├── 📄 README.md           # Apresentação geral e guia do repositório
└── 📄 requirements.txt    # Lista de dependências e bibliotecas do projeto

```

---

## 8. Equipe

- [Antônio Marcel](https://github.com/MarcelProgram)
- [Edivaldo Dias](https://github.com/Edy-Ap-Dias)
- [Leonardo Gomes](https://github.com/LeonardoFGs)
- [Leonardo Santos](https://github.com/leojosants)
- [Vanessa Vilela](https://github.com/vsvilela39-oss)
- [Vitor Pires](https://github.com/vikpires)
