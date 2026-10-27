# Preditor de Preços de Imóveis

Um projeto de Machine Learning e Deep Learning que engloba todo o ciclo de vida dos dados: desde a limpeza e engenharia de atributos até a implantação de uma aplicação web conteinerizada com monitoramento de experimentos.

## Sobre o Projeto

Este projeto foi desenvolvido para prever o preço de imóveis com base no *Housing Prices Dataset*. O principal objetivo é demonstrar a construção de um pipeline completo de dados, passando pela análise exploratória, validação estatística, modelagem preditiva, e por fim, a produtização do modelo.

## Stack

**Ciência de Dados & Machine Learning:**
*   **Manipulação e Análise:** Pandas, NumPy
*   **Visualização:** Matplotlib, Plotly, Seaborn
*   **Machine Learning/Deep Learning:** Scikit-Learn, PyTorch
*   **Rastreamento de Experimentos:** MLflow

**MLOps:**
*   **Backend:** FastAPI
*   **Frontend:** Streamlit
*   **Orquestração e Deploy:** Docker, Docker Compose

---

## Arquitetura do Sistema & Workflow

A aplicação foi desenhada em uma arquitetura conteinerizada com Docker, integrando o rastreamento de experimentos ao fluxo de consumo e predição em tempo real.

| Arquitetura da Aplicação | Workflow |
| :---: | :---: |
| ![Arquitetura do Sistema](docs/images/architecture.png) | ![Workflow de Dados](docs/images/workflow.png) |

### Funcionamento dos Componentes:
1. **Frontend (Streamlit):** Interface interativa onde o usuário insere as características do imóvel.
2. **Backend (FastAPI):** API REST que recebe os dados, processa e retorna a previsão de preço.
3. **MLflow:** Utilizado para registrar e monitorar os hiperparâmetros e métricas de desempenho durante a experimentação de Redes Neurais.

---

## Interface Web

Abaixo estão as capturas de tela da interface desenvolvida em Streamlit para interação com o usuário final:

| Entrada de Dados | Exibição da Predição |
| :---: | :---: |
| ![Interface - Entrada de Dados](docs/images/app_inputs.png) | ![Interface - Resultado Predito](docs/images/app_prediction.png) |

---

## Pipeline de Dados (Fases do Projeto)

<details>
<summary><b>Fase 1 — Limpeza e Padronização</b></summary>
Consolidação e tipagem de dados, tratamento de valores ausentes e padronização de variáveis categóricas (localização e tipo do imóvel).
</details>

<details>
<summary><b>Fase 2 — Consultas e Agregações</b></summary>
Análise histórica de preços, análises localizadas por bairro e levantamento do ranking dos cinco bairros com maiores valores médios.
</details>

<details>
<summary><b>Fase 3 — Estatística e Outliers</b></summary>
Identificação de valores atípicos nos preços e avaliação se representam comportamento real de mercado ou inconsistências de coleta.
</details>

<details>
<summary><b>Fase 4 — Visualização e Análise Exploratória (EDA)</b></summary>
Mapeamento da relação entre área e preço, além da comparação da evolução temporal dos valores médios.
</details>

<details>
<summary><b>Fase 5 — Engenharia de Atributos e Correlações</b></summary>
Criação de novas variáveis derivadas, análise de correlação com o preço alvo e transformação de variáveis categóricas em formatos numéricos.
</details>

<details>
<summary><b>Fase 6 — Machine Learning</b></summary>
Construção do modelo preditivo de regressão para identificar as principais variáveis de influência e agrupamento (clustering) de imóveis/bairros.
</details>

<details>
<summary><b>Fase 7 — Deep Learning</b></summary>
Preparação dos dados, implementação, treinamento e avaliação de arquiteturas de redes neurais com registro completo no MLflow.
</details>

---

## Experimentos com Redes Neurais (MLflow)

Para otimizar a predição, foram executados e comparados três experimentos de arquiteturas de redes neurais com 200 épocas de treinamento:
* `RedeNeuralV1_200_Epochs`
* `RedeNeuralV2_200_Epochs`
* `Real_State_Deep_Model_200_Epochs`

### Avaliação da Métrica $R^2$ (%)

O modelo RedeNeuralV2_200_Epochs destacou-se com o melhor desempenho geral, alcançando aproximadamente 84% de $R^2$ em teste e 86% em treino.

| Treino ($R^2$) | Teste ($R^2$) |
| :---: | :---: |
| ![Métrica R2 no Treino](docs/images/r2_train_percent.png) | ![Métrica R2 no Teste](docs/images/r2_test_percent.png) |

### Avaliação da Função de Perda (MSE Loss)

A análise da curva de erro quadrático médio comprova a convergência do modelo vencedor.

| Treino (MSE Loss) | Teste (MSE Loss) |
| :---: | :---: |
| ![MSE Loss no Treino](docs/images/train_loss_mse.png) | ![MSE Loss no Teste](docs/images/test_loss_mse.png) |

## Autor

Desenvolvido por **Lucas Belmonte Alves**.