# Self-Engenharia-de-dados-Roadmap

#### Fase 1: **[Fundamentos de SQL](https://github.com/johanngomig/Self-Engenharia-de-dados-Roadmap/tree/main/Query-SQL) e [Python](https://github.com/johanngomig/Self-Engenharia-de-dados-Roadmap/tree/main/Python/Fase%201)**
Objetivo: Dominar o SQL e manipulação de dados em Python.

**SQL:**
1. **Teoria e Prática de SQL Avançado**:
   - Revisão de joins: INNER, OUTER, LEFT, RIGHT.
   - Exercícios práticos sobre **funções de agregação** avançadas (ex: HAVING, COUNT DISTINCT).
   - **CTEs e Subqueries**: prática com consultas aninhadas e uso de expressões comuns.

**Exercício**:
- Criar um banco de dados simulado com diferentes tabelas e praticar os joins entre elas.
- Implementar consultas complexas que envolvam **group by**, **CTEs** e **subqueries**.

**Python:**
1. **Manipulação de Dados com pandas**:
   - Foco em operações com DataFrames: filtragem, agregação e limpeza de dados.
   - Estruturas de dados: listas, dicionários e arrays multidimensionais.
   - Introdução ao **NumPy** para operações numéricas.

**Exercício**:
- Carregar um dataset público.
- Realizar operações de limpeza, agregação e geração de insights a partir dos dados.

---

#### Fase 2: **Data Pipelines e Modelagem de Dados**
Objetivo: Construir pipelines de dados e entender a modelagem de sistemas.

**Data Pipelines**:
1. **Introdução ao Apache Airflow**:
   - Conceito de orquestração de pipelines.
   - Criar e agendar pipelines simples.

2. **ETL/ELT**:
   - Criar um pipeline ETL usando Python e pandas.

**Exercício**:
- Criar um pipeline de ETL que extrai dados de um CSV, transforma-os e armazena o resultado em uma base de dados simulada.

**Modelagem de Dados**:
1. **Teoria sobre Modelagem de Dados**:
   - Revisão de **esquema estrela** e **floco de neve**.
   - Prática com ferramentas como **dbdiagram.io** para modelagem visual de bancos de dados.

**Exercício**:
- Modelar o esquema de um data warehouse utilizando o conceito de **esquema estrela**.

---

#### Fase 3: **Big Data e Processamento em Nuvem**
Objetivo: Trabalhar com grandes volumes de dados e processamento em tempo real.

**Big Data**:
1. **Introdução ao Apache Spark**:
   - Fundamentos do processamento distribuído.
   - Implementar processamento em batch e streaming com **PySpark**.

**Exercício**:
- Carregar um grande dataset no Databricks e realizar operações de processamento em batch com **PySpark**.

**Cloud Computing**:
1. **Conceitos de Armazenamento e Processamento em Nuvem**:
   - Introdução ao **Google Cloud** e uso do **BigQuery**.
   - Criar um banco de dados na nuvem, carregar dados e executar consultas SQL.

**Exercício**:
- Utilizar o **Google Cloud Free Tier** para criar uma instância de BigQuery, carregar dados e realizar consultas sobre grandes volumes de dados.

---

#### Fase 4: **Preparação para Entrevista**
Objetivo: Revisar e praticar para entrevistas técnicas de engenheiro de dados.

1. **Revisão de SQL**:
   - Praticar consultas complexas usando **LeetCode** e **HackerRank**.
   - Resolver problemas de SQL que simulam situações reais de trabalho.

2. **Desafio Final**:
   - Construir um pipeline completo de ETL, integrando o processamento de dados com Airflow e Spark, e armazenando os resultados em um data warehouse simulado.

---
