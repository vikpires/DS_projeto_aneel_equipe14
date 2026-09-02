 <div align="center">
   <img src=".\docs\assets\energy_towers.jpg" width=100% alt="Imagem de torres de energia elétrica" /> 
 </div>

# Análise de Dados de Continuidade Elétrica e Previsão de Risco Regulatório (ANEEL)

<p align="left">
  <!-- Linguagem & Ambientes -->
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge" alt="Matplotlib" />
  <img src="https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge" alt="Seaborn" />  
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" alt="Power BI" />
</p>

---

## Descrição
Projeto de **Análise de Dados e Machine Learning** desenvolvido sobre dados públicos da Agência Nacional de Energia Elétrica (ANEEL), com foco no diagnóstico dos indicadores de continuidade do fornecimento elétrico (DEC e FEC) e na mitigação de riscos e compensações regulatórias no Brasil. Trabalho desenvolvido como projeto prático da formação **AI Talent Academy**, da *White Cube*.

---

## Sumário
- [1. Contexto](#1-contexto)
- [2. Objetivo](#2-objetivo)
- [3. Base de Dados](#3-base-de-dados)
- [4. Metodologia](#4-metodologia)
- [5. Cronograma e Fases](#5-cronograma-e-fases)
- [6. Organização dos Diretorios](#6-organização-dos-diretórios)
- [7. Desenvolvedores](#7-desenvolvedores)

---

## 1. Contexto
No setor de distribuição de energia elétrica no Brasil, a **Agência Nacional de Energia Elétrica (ANEEL)** estabelece metas e padrões contratuais estritos de qualidade por meio de dois indicadores coletivos de continuidade:

* **DEC (Duração Equivalente de Interrupção por Unidade Consumidora):** Mede o tempo médio (em horas) que os consumidores atendidos por determinado conjunto ficaram sem energia.

* **FEC (Frequência Equivalente de Interrupção por Unidade Consumidora):** Mede a quantidade média de vezes em que ocorreram interrupções no fornecimento.

A transgressão desses limites regulatórios acarreta compensações financeiras obrigatórias repassadas diretamente na fatura dos consumidores afetados, impactando a receita operacional líquida das concessionárias e sua reputação institucional.

---

## 2. Objetivo
Construir uma solução de análise de dados capaz de:

- Analisar a evolução dos indicadores DEC e FEC;
- Comparar os valores realizados com os limites regulatórios;
- Identificar conjuntos consumidores com maior incidência de transgressões;
- Analisar os principais grupos e causas das interrupções;
- Identificar padrões temporais e operacionais;
- Relacionar causas de interrupções ao comportamento dos indicadores de continuidade;
- Desenvolver um modelo de Machine Learning para estimar o risco de transgressão futura.

---

## 3. Base de Dados
Os dados utilizados são públicos e extraídos do portal de dados abertos da ANEEL:

* **Dataset:** [Indicadores Coletivos de Continuidade (DEC e FEC)](https://dadosabertos.aneel.gov.br/pt_BR/dataset/indicadores-coletivos-de-continuidade-dec-e-fec)
* **Métricas Principais:** Valores apurados, limites regulatórios mensais e anuais contratados.

---

## 4. Metodologia

O projeto adotará o framework **CRISP-DM**, estruturado em seis fases:

1. **Compreensão do Negócio (Business Understanding):** Mapeamento das regras regulatórias (PRODIST/ANEEL), impacto financeiro das compensações por violação de DEC/FEC, definição de KPIs de negócio, métricas técnicas e escopo do projeto.

2. **Compreensão dos Dados (Data Understanding):** Ingestão das bases anuais, auditoria de integridade e Análise Exploratória de Dados (EDA).

3. **Preparação dos Dados (Data Preparation):** Limpeza, padronização e estruturação do modelo dimensional.

4. **Modelagem (Modeling):** Desenvolvimento da camada analítica de medidas em DAX e modelagem preditiva de risco regulatório.

5. **Avaliação (Evaluation):** Auditoria das regras de agregação e validação de desempenho dos modelos.

6. **Implantação (Deployment) & Demo Day:** Desenvolvimento do relatório executivo no Power BI, documentação técnica e apresentação final.

---

## 5. Cronograma e Fases
<p align="left">
  <a href="https://github.com/users/vikpires/projects/7/views/4?sliceBy[columnId]=Milestone">
    <img src="https://img.shields.io/badge/Backlog_&_Roadmap-1074e7?style=for-the-badge&logo=github&logoColor=white" alt="Backlog e Roadmap" />
  </a>
</p>

| Fase / Marco | Status | Período | Tarefas |
| :--- | :---: | :---: | :---: |
| **01:  Compreensão do Negócio (Business Understanding)** | Em Progresso | Semana 4 | [Ver Tarefas](https://github.com/vikpires/ai_academy_final_challenge/milestone/1) |
| **02: Compreensão dos Dados (Data Understanding)** | Em Progresso | Semana 5 | [Ver Tarefas](https://github.com/vikpires/ai_academy_final_challenge/milestone/6) |
| **03: Preparação dos Dados (Data Preparation)** | A Iniciar | Semana 6 | [Ver Tarefas](https://github.com/vikpires/ai_academy_final_challenge/milestone/2) |
| **04: Modelagem (Modeling)** | A Iniciar | Semana 7 | [Ver Tarefas](https://github.com/vikpires/ai_academy_final_challenge/milestone/3) |
| **05: Avaliação (Evaluation)** | A Iniciar | Semana 8 | [Ver Tarefas](https://github.com/vikpires/ai_academy_final_challenge/milestone/4) |
| **06: Implantação (Deployment) & Demo Day** | A Iniciar | Semana 8 | [Ver Tarefas](https://github.com/vikpires/ai_academy_final_challenge/milestone/5) |

---

## 6. Organização dos Diretórios

```markdown
├── 📁 data/
│   ├── 📁 raw/            # Dados brutos originais
│   ├── 📁 external/       # Dados externos e bases de apoio
│   └── 📁 processed/      # Dados finais tratados para análise e modelagem
│
├── 📁 docs/               # Documentação do projeto, escopo e dicionário de dados
│    ├── 📁 assets/        # Imagens e diagramas para documentação
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

## 7. Desenvolvedores

 - [Antônio Marcel](https://github.com/MarcelProgram)
 - [Edivaldo Dias](https://github.com/Edy-Ap-Dias)
 - [Leonardo Gomes](https://github.com/LeonardoFGs)
 - [Leonardo Santos](https://github.com/leojosants)
 - [Vanessa Vilela](https://github.com/vsvilela39-oss)
 - [Vitor Pires](https://github.com/vikpires)
