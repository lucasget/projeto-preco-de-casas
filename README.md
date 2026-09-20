# Preditor de Preços de Imóveis

Um projeto *ponta a ponta* de Machine Learning e Deep Learning que engloba todo o ciclo de vida dos dados: desde a limpeza e engenharia de atributos até a implantação de uma aplicação web conteinerizada com monitoramento de experimentos.

## Sobre o Projeto

Este projeto foi desenvolvido para prever o preço de imóveis com base no *Housing Prices Dataset*. O principal objetivo é demonstrar a construção de um pipeline completo de dados, passando pela análise exploratória, validação estatística, modelagem preditiva e, por fim, a produtização do modelo.

## Stack

**Ciência de Dados & Machine Learning:**
*   **Manipulação e Análise:** Pandas, NumPy
*   **Visualização:** Matplotlib, Plotly
*   **Machine Learning/Deep Learning:** Scikit-Learn, PyTorch, Joblib 
*   **Rastreamento de Experimentos:** MLFlow

**Engenharia de Software & DevOps:**
*   **Backend:** FastAPI
*   **Frontend:** Streamlit
*   **Orquestração e Deploy:** Docker, Docker Compose

## Arquitetura do Sistema

O projeto adota uma arquitetura em microsserviços, garantindo o isolamento e escalabilidade da aplicação:

1.  **Frontend (Container 1):** Uma interface interativa construída com Streamlit, onde o usuário insere as características do imóvel.
2.  **Backend (Container 2):** Uma API REST construída com FastAPI que recebe os dados do front, processa no modelo treinado e retorna a previsão de preço.
3.  **MLFlow:** Integrado para rastrear o histórico de treinamento, hiperparâmetros e métricas de desempenho da Rede Neural.

## Pipeline de Dados (Fases do Projeto)

<details>
<summary><b>Fase 1: Limpeza e Padronização</b></summary>
Consolidação de tipos de dados, tratamento de valores ausentes e correção de inconsistências nas variáveis categóricas como localização e tipo do imóvel.
</details>

<details>
<summary><b>Fase 2: Consultas e Agregações</b></summary>
Análise do comportamento histórico do mercado.
</details>

<details>
<summary><b>Fase 3: Estatística e Outliers</b></summary>
Identificação de valores atípicos nos preços e análise para definir se representam casos reais de mercado ou inconsistências de coleta.
</details>

<details>
<summary><b>Fase 4: Visualização e Análise Exploratória (EDA)</b></summary>
Mapeamento de padrões entre área construída e preço final, além do acompanhamento da evolução temporal dos valores.
</details>

<details>
<summary><b>Fase 5: Engenharia de Atributos e Correlações</b></summary>
Criação de atributos derivados para enriquecer a base, mapeamento das variáveis com maior impacto no preço alvo.
</details>

<details>
<summary><b>Fase 6: Machine Learning</b></summary>
Treinamento do modelo preditivo base (Regressão), avaliação das *features* mais importantes.
</details>

<details>
<summary><b>Fase 7: Deep Learning</b></summary>
Estruturação dos dados para redes neurais, implementação da arquitetura da rede, e registro dos experimentos utilizando MLFlow.
</details>


## Autor

Desenvolvido por **Lucas Belmonte Alves**. 