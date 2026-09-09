# Escopo do Projeto

* **Projeto:** ANEEL — Energia em Risco 

* **Documento:** Escopo do Projeto e Entendimento do Negócio (CRISP-DM Fase 1)

* **Data de Elaboração:** 09/2026

* **Versão:** 1.1

---

## Sumário

- [1. Dados do Projeto ](#1-dados-do-projeto)
- [2. Visão Geral](#2-visão-geral)
- [3. Proposta do Projeto](#3-proposta-do-projeto)
    - [3.1. Contextualização](#31-contextualização)
    - [3.2. Problema](#32-problema)
    - [3.3. Objetivo Geral](#33-objetivo-geral)
    - [3.4. Objetivos Específicos](#34-objetivos-específicos)
- [4. Metodologia](#4-metodologia)
- [5. Usuários e Matriz de Stakeholders](#5-usuários-e-matriz-de-stakeholders)
- [6. Dados Necessários e Fontes](#6-dados-necessários-e-fontes)
- [7. Hipóteses do Projeto](#7-hipóteses-do-projeto)
- [8. Riscos](#8-riscos)
- [9. Fora de Escopo](#9-fora-de-escopo)
- [10. Estrutura de Custos](#10-estrutura-de-custos)
- [11. Solução](#11-solução)
- [12. Métricas de Avaliação e Benchmarks de Sucesso](#12-métricas-de-avaliação-e-benchmarks-de-sucesso)
- [13. Requisitos e Restrições ](#13-requisitos-e-restrições)
- [14. Entregáveis](#14-entregáveis)
- [15. Síntese Executiva](#15-síntese-executiva)

---

## 1. Dados do Projeto 

* **Título:** Projeto ANEEL — Energia em Risco: Análise dos Indicadores DEC/FEC e Predição de Transgressões no Sistema de Distribuição de Energia

* **Equipe Responsável:** Equipe 14 - Antônio Marcel, Edivaldo Dias, Leonardo Gomes, Leonardo Santos, Vanessa Vilela, Vitor Pires

* **Metodologia de Gestão:** CRISP-DM e a metodologia ágil Kanban

* **Repositório Oficial:** [Repositório do Projeto](https://github.com/vikpires/projeto_aneel_equipe14) | (Branch padrão: `develop`)

* **Quadro Kanban:** [Kanban_projeto_aneel_equipe14](https://github.com/users/vikpires/projects/7/views/1)

* **Período de Execução:** 01/09/2026 a 30/09/2026 

---

## 2. Visão Geral
Este documento consolida a **Fase 1 do CRISP-DM - Compreensão do Negócio (Business Understanding)**. Sua finalidade é formalizar o alinhamento estratégico, mapear as dores do setor elétrico e fixar critérios técnicos mensuráveis antes da manipulação dos dados brutos no pipeline de dados.

---

## 3. Proposta do Projeto

Elaborar uma solução analítica e preditiva para diagnosticar, monitorar e prever transgressões nos indicadores de continuidade do fornecimento de energia elétrica (DEC e FEC) estipulados pela Agência Nacional de Energia Elétrica (ANEEL).

#### 3.1. Contextualização
A distribuição de energia elétrica no Brasil opera sob regime de concessão pública regulada pela ANEEL. A conformidade dos serviços prestados pelas distribuidoras é fiscalizada segundo os critérios do **PRODIST (Procedimentos de Distribuição de Energia Elétrica no Sistema Elétrico Nacional)**, que estabelece padrões rígidos de qualidade comercial e de continuidade do fornecimento.

A ANEEL acompanha essa qualidade por meio de indicadores regulatórios que permitem medir a duração e a frequência das interrupções percebidas pelos consumidores. Os indicadores centrais utilizados neste projeto são:

* **DEC (Duração Equivalente de Interrupção por Unidade Consumidora):** Mede o tempo médio acumulado, em horas, que os consumidores de um conjunto ficaram sem fornecimento elétrico em um determinado intervalo de tempo.

* **FEC (Frequência Equivalente de Interrupção por Unidade Consumidora):** Mede a quantidade média de vezes em que ocorreram interrupções no fornecimento para os consumidores desse mesmo conjunto.

Para cada conjunto e período de apuração, a ANEEL publica os valores de **Limite DEC** e **Limite FEC**. Quando uma distribuidora apura índices superiores a essas metas (Apurado > Limite), comete-se uma **transgressão regulatória**. Essa violação obriga a concessionária a creditar compensações financeiras automáticas na fatura dos consumidores afetados, além de elevar o risco de autuações administrativas e comprometer a reputação da companhia perante o mercado e os órgãos de controle.

#### 3.2. Problema
A gestão de continuidade do serviço nas concessionárias opera frequentemente de forma **reativa**: as violações só são diagnosticadas após o fechamento do período regulatório, quando o prejuízo financeiro e as compensações aos consumidores já estão consolidados.

A solução proposta visa apoiar as seguintes decisões críticas de negócio:

* **Transição da Gestão Reativa para Preventiva:** Mudar o foco da apuração retroativa de multas para a antecipação de conjuntos elétricos com risco iminente de transgressão.

* **Mitigação de Passivos Financeiros:** Reduzir o volume de créditos e indenizações diretas pagas aos consumidores por descumprimento de metas regulatórias do PRODIST Módulo 8.

* **Monitoramento Executivo Contínuo:** Fornecer à alta liderança e analistas regulatórios uma visão clara da evolução histórica da conformidade por distribuidora e região.

#### 3.3. Objetivo Geral
Construir uma solução integrada de Análise de Dados e Machine Learning que permita analisar o comportamento histórico dos indicadores DEC e FEC, diagnosticar reincidências de transgressões e estimar a probabilidade de descumprimento dos limites regulatórios futuros em nível de conjunto consumidor.

#### 3.4. Objetivos Específicos
* Consolidar a série histórica (2021–2025) dos dados de continuidade da ANEEL

* Comparar os valores apurados com os limites regulatórios, mapeando taxas de transgressão e gerando ranking dos conjuntos elétricos mais críticos.

* Identificar comportamentos cíclicos e disparidades regionais no desempenho operacional.

* Treinar e avaliar um modelo de Machine Learning supervisionado para classificar o risco de violação (Apurado > Limite) de conjuntos elétricos no horizonte mensal subsequente.

* Disponibilizar os diagnósticos, estimativas de passivo financeiro e scores de risco preditivo em dashboards interativos no Power BI sob modelagem *Star Schema*.

---

### 4. Metodologia

O projeto adotará o framework **CRISP-DM**, estruturado em seis fases:

1. **Compreensão do Negócio (Business Understanding):** Mapeamento das regras regulatórias (PRODIST/ANEEL), impacto financeiro das compensações por violação de DEC/FEC, definição de KPIs de negócio, métricas técnicas e escopo do projeto.

2. **Compreensão dos Dados (Data Understanding):** Ingestão das bases anuais, auditoria de integridade e Análise Exploratória de Dados (EDA).

3. **Preparação dos Dados (Data Preparation):** Limpeza, padronização e estruturação do modelo dimensional.

4. **Modelagem (Modeling):** Desenvolvimento da camada analítica de medidas em DAX e modelagem preditiva de risco regulatório.

5. **Avaliação (Evaluation):** Auditoria das regras de agregação e validação de desempenho dos modelos.

6. **Implantação (Deployment) & Demo Day:** Desenvolvimento do relatório executivo no Power BI, documentação técnica e apresentação final.

### 5. Usuários e Matriz de Stakeholders

**Quem toma a decisão hoje?**  

* **Gestores de Distribuidoras (Regulação e Diretoria):** Decidem provisões financeiras, prestam contas à ANEEL e definem estratégias corporativas para cumprimento do contrato de concessão.

* **Operação e Manutenção (O&M):** Decidem a priorização de vistorias técnicas, alocação de equipes de campo e planos de melhoria na rede de distribuição.

**Quem é afetado?**  

* **Consumidores Finais:** Sofrem diretamente com a falta de energia e recebem as compensações financeiras em fatura.

* **Concessionária:** Sofre com o passivo financeiro imediato das compensações e o desgaste de imagem institucional.

* **Times Técnicos (Analistas de Dados/BI e Cientistas de Dados):** São cobrados por diagnósticos rápidos e relatórios confiáveis para justificar desvios aos órgãos de controle.

**Matriz de Stakeholders**

| Stakeholder | Papel na Tomada de Decisão | Dores Principais | Uso da Solução |
| :--- | :--- | :--- | :--- |
| **Gestores de Distribuidoras** | Decisor Estratégico | Dificuldade em prever o passivo de multas e falta de visão consolidada do cumprimento contratual | Acompanhamento do dashboard executivo para monitorar taxas de transgressão e projetar custos regulatórios antes do fechamento oficial. |
| **Operação e Manutenção (O&M)** | Decisor Operacional | Atuação reativa e falta de critério preditivo para priorizar quais conjuntos elétricos devem receber vistorias preventivas | Utilização do score de risco de Machine Learning para direcionar cronogramas preventivos nos conjuntos com alta probabilidade de estouro |
| **Analistas de Dados/BI** | Usuário Analítico | Bases da ANEEL pesadas e despadronizadas; lentidão para atualizar relatórios operacionais no Power BI. | Acesso a dados modelados em Star Schema via Parquet de alta performance, agilizando relatórios e auditorias. |
| **Cientistas de Dados** | Usuário Técnico | Falta de dados limpos para modelagem preditiva e necessidade de retreino periódico dos modelos. | Pipeline reprodutível com histórico sazonal e métricas padronizadas |

---

### 6. Dados Necessários e Fontes 

**Dados Necessários**  
* Dados dos indicadores: DEC e FEC apurados, limites regulatórios mensais/anuais, valores de compensação financeira e identificador da distribuidora.

* Dados complementares: Código e nome do conjunto de unidades consumidoras, quantidade de clientes atendidos, região geográfica/UF, subestação de atendimento e histórico cadastral.

* Dados derivados: Médias móveis, taxas de variação mensal, contagem de reincidência de violações consecutivas, índices de sazonalidade e score preditivo de risco de transgressão.

**Fonte de Dados**  
Os dados são de origem pública e extraídos do **Portal de Dados Abertos da ANEEL** e do arcabouço normativo do **PRODIST**. Para fins de análise, o conjunto de dados será limitado a um período de 5 anos (2021-2025):

| Entidade / Recurso | Fonte Oficial | Periodicidade / Granularidade | Uso no Projeto |
| :--- | :--- | :--- | :--- |
| **Indicadores Coletivos de Continuidade (DEC e FEC)** | [Portal de Dados Abertos da ANEEL](https://dadosabertos.aneel.gov.br/pt_BR/dataset/indicadores-coletivos-de-continuidade-dec-e-fec) | Mensal / Anual por Conjunto Elétrico | Dados brutos de DEC e FEC (apurado e limites regulatórios) para métricas de BI e alvo do ML. |
**Interrupções de Energia Elétrica nas Redes de Distribuição** | [Portal de Dados Abertos da ANEEL](https://dadosabertos.aneel.gov.br/pt_BR/dataset/interrupcoes-de-energia-eletrica-nas-redes-de-distribuicao) | Por evento / Ocorrência | Mapeamento da tipologia de causas das quedas (acidentais, programadas, expurgos regulatórios). |
| **Regras e Parâmetros Regulatórios** | [ANEEL — PRODIST Módulo 8](https://www.gov.br/aneel/pt-br/centrais-de-conteudos/procedimentos-regulatórios/prodist) | Regulatório / Estático | Fórmulas conceituais de transgressão e parâmetros para cálculo da proxy de compensações financeiras. |

**Armazenamento e Formato**  
Arquivos originais em `.csv`/`.parquet` mantidos fora do versionamento do Git, processados via DuckDB e salvo como Parquet otimizado na pasta `data/interim/` e `data/processed/`.

**Privacidade e LGPD:** 
100% dos dados são operacionais e anonimizados na fonte pela ANEEL, sem exposição de dados pessoais ou faturas individualizadas.

---

### 7. Hipóteses do Projeto 

* **Hipótese 01** - Conjuntos com histórico crônico de transgressão de DEC e FEC apresentam probabilidade significativamente maior de ultrapassar os limites regulatórios nos períodos seguintes.

* **Hipótese 02** - Interrupções não programadas possuem maior impacto no tempo acumulado de desabastecimento (DEC) em comparação às paradas programadas para manutenção.

* **Hipótese 03** - Existe sazonalidade nas interrupções, com meses e regiões mais propensos à piora da continuidade.

* **Hipótese 04** - O volume de unidades consumidoras atendidas e o perfil geográfico do conjunto influenciam diretamente o desempenho dos indicadores de continuidade.

* **Hipótese 05** - O histórico recente de DEC, FEC e do volume de interrupções pode ser utilizado para prever o risco de transgressão regulatória no período subsequente.

---

### 8. Riscos

1. **Risco de Dados**
    * Dados faltantes ou nulos, com ausência de registros pontuais em limites ou apurações de conjuntos desativados/reestruturados.

    * Inconsistências temporais e cadastrais, com mudança de identificador do conjunto elétrico ou alterações de metodologia cadastral ao longo dos anos.

    * Granularidade desigual, contendo conflito entre dados agregados mensalmente (DEC/FEC) e dados por ocorrência (interrupções individuais).

2. **Risco de Modelagem e Machine Learning**
    * Volume de meses em conformidade muito superior ao de transgressões, induzindo o modelo a prever sempre a classe majoritária.

    *  O algoritmo memorizar o comportamento (overfitting) de distribuidoras específicas sem conseguir prever o risco em novas regiões.

    * Uso de acurácia global em vez de métricas mais robustas (Recall, PR-AUC e F1-Score).

3. **Risco de Projeto e Negócio**
    * Gerar *insights* estatísticos avançados, mas que não auxiliam a tomada de decisão prática da equipe de manutenção.

    * Confundir correlação de variáveis operacionais com causalidade regulatória.

    * Não considerar alterações ou revisões tarifárias/metas aprovadas pela ANEEL no período.

---

### 9. Fora de Escopo

* Não serão manipulados dados individualizados por consumidor, garantindo conformidade com a LGPD.

* A solução não definirá reajustes de tarifa de energia nem estratégias de cobrança ou faturamento.

* O projeto se encerra na entrega do modelo validado com previsões salvas em lote e dashboard no Power BI.

* Não serão integradas APIs meteorológicas em tempo real e arquivos da BDGD (redes elétricas/postes).

* Ausência de banco de dados corporativo dedicado ou cluster em nuvem (arquitetura desacoplada baseada em arquivos Parquet).

---

### 10. Estrutura de custos 

* **Fontes de Dados:** Gratuitas (Portal de Dados Abertos da ANEEL sob licença pública).

* **Infraestrutura Computacional:** Execução em máquinas locais dos membros da equipe e instâncias gratuitas em nuvem (Google Colab / GitHub).

* **Esforço Humano (Custo Operacional):** Dedicação de 6 membros ao longo do ciclo do projeto, distribuídos entre engenharia de dados, modelagem preditiva, construção do dashboard e documentação.

* **Manutenção Futura (Evolutivo):** Esforço periódico estimado em poucas horas/mês para reexecução do script de download, atualização de novos meses da ANEEL e retreino semestral do modelo.

---

### 11. Solução

* Pipeline automatizado em Python/DuckDB para ingestão, tratamento de dados nulos, padronização de esquemas, criação de variáveis temporais (médias móveis, defasagens/lags e tendências) e exportação no formato `.parquet`.

* Análise exploratória de Dados (EDA), com identificação de padrões, tendências e possíveis relações entre variáveis.

* Modelo supervisionado de classificação tabular executado em lote (*batch*), gerando scores de probabilidade de violação regulatória para cada conjunto elétrico no período subsequente.

* Painel interativo em Power BI.

---

### 12. Métricas de Avaliação e Benchmarks de Sucesso

1. **Qualidade e Integridade dos Dados:**
   * **Percentual de Valores Ausentes:** Registros sem preenchimento em campos críticos (`DEC`, `FEC`, `Limites` e `IDs de Conjunto`) inferiores a **1%**.

   * **Consistência Temporal e Duplicidade:** Manter **0%** de duplicidade na granularidade chave (`Conjunto` + `Mês/Ano`) em todo o histórico de 2021 a 2025.

   * **Taxa de Registros Válidos:** Pelo menos **98%** das linhas em conformidade com as regras operacionais da ANEEL.

2. **Eficácia da Análise e Visualização:**
   * **Cobertura Cadastral:** **100%** das distribuidoras e conjuntos elétricos da base processada navegáveis no painel.

   * **Identificação de Concentração:** Mapeamento quantitativo comprovando a concentração de horas excedentes nos conjuntos mais críticos.

   * **Performance e Navegação:** Painel em Power BI estruturado em *Star Schema* com filtros dinâmicos e tempo de resposta inferior a **5 segundos** por interação.

3. **Desempenho do Modelo Preditivo (Machine Learning):**
   * **Recall (Sensibilidade) $\ge 75\%$:** Capacidade de antecipar a maioria das transgressões reais antes do fechamento do mês, minimizando multas surpresa.

   * **Precisão $\ge 60\%$:** Garantir que pelo menos 3 a cada 5 alertas emitidos pelo modelo correspondam a problemas reais, evitando deslocamento inútil de equipes.

   * **F1-Score ($\ge 0,65$ a $0,70$):** Balanço harmônico entre capturar o risco regulatório e não saturar a operação com alarmes falsos.

   * **PR-AUC e ROC-AUC ($\ge 0,80$):** Capacidade geral do modelo de ordenar e separar corretamente os conjuntos de alto risco dos conjuntos estáveis.

   * **Matriz de Confusão Calibrada:** Ajuste do limiar de decisão (*threshold*) priorizando a redução expressiva de falsos negativos (transgressões não previstas).

4. **Impacto e Acionabilidade de Negócio**
    * **Foco no Top Risco (Lift Operacional):** O modelo deve concentrar pelo menos 60% das transgressões reais do mês seguinte dentro dos 20% dos conjuntos sinalizados com maior probabilidade de violação.

    * **Priorização Acionável:** Geração de um ranking mensal dos conjuntos elétricos com maior urgência de vistoria preventiva.

    * **Simulação de Redução de Passivos:** Quantificação financeira das compensações regulatórias potencialmente evitadas caso as manutenções atuem a tempo nos conjuntos sinalizados.

---

### 13. Requisitos e Restrições 

| **Requisitos Funcionais (RF)** |
|:---|
| **RF01:** O pipeline deve consolidar os dados mensais de continuidade (DEC e FEC) de 2021 a 2025. | 
| **RF02:** O sistema deve calcular o indicador booleano de transgressão (Apurado > Limite) e a margem de desvio relativo para cada conjunto/mês. |
| **RF03:** A camada de dados deve alimentar o Power BI com um modelo dimensional (*Star Schema*) contendo tabelas fato e dimensão documentadas.|
| **RF04:** O modelo de Machine Learning deve gerar uma coluna contendo o *Score de Risco* (probabilidade entre 0 e 1) de descumprimento para o período `t+1`.|

| **Requisitos Não Funcionais (RNF)**
|:---|
| **RNF01:** Scripts de dados e modelagem versionados no Git com arquivo `requirements.txt` e ambiente virtual configurado. |
| **RNF02:** Processamento de arquivos pesados via DuckDB em disco, sem exceder 4 GB de memória RAM local.| 
| **RNF03:** Estrita aderência à LGPD, não utilizando registros de consumo ou dados pessoais identificáveis.|

---

### 14. Entregáveis

1. **Repositório de Código Documentado (GitHub):**

   * Código de ingestão e transformação automatizado em DuckDB/Python.

   * Pipeline de treino, validação e inferência em lote de Machine Learning.

   * Arquivo `README.md` com instruções detalhadas de reprodução do ambiente.


2. **Camada de Dados Otimizada (Data Lake Local):**

   * Bases consolidadas em Apache Parquet nas pastas `data/interim/` e `data/processed/` (*Star Schema* e dataset pronto para treino de ML).


3. **Análise Exploratória de Dados (EDA):**

   * Notebooks documentados com o diagnóstico descritivo do DEC e FEC, análise de sazonalidade, concentração de queixas e validação estatística das hipóteses levantadas.


4. **Dashboard Executivo e Operacional (Power BI):**

   * Relatório interativo `.pbix` integrando diagnóstico histórico de DEC/FEC, análise de causas e o score preditivo de transgressão.


5. **Relatório Técnico e Apresentação Executiva:**

   * Síntese metodológica contendo a validação das hipóteses, métricas do modelo preditivo e recomendações práticas de negócio.

---

### 15. Síntese Executiva 

 <div align="center">
   <img src=".\assets\data_canvas.png" width=100% alt="Canvas do Problema de Dados" />
   <sub>Canvas do Problema de Dados</sub><br /> 
   <sub>Fonte: Elaborado pelos autores</sub> 
 </div>
 