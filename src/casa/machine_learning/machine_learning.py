import joblib
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error


#calcular_correlacao(df_modelo)
def plot_todas_distribuicoes(df):
     sns.pairplot(df, diag_kind='kde')
     plt.show()


def treinar_e_plotar_modelo(df):
     x = df.drop(columns = 'preco')
     y = df['preco']
     # usando degree = 2 para não aumentar muito a complexidade do modelo e assim ele decorar os dados, 
     # bias = False pq a classe LinearRegression ja calcula o viés automaticamente
     poly = PolynomialFeatures(degree=2, include_bias=False)
     x_poly = poly.fit_transform(x)
     x_train, x_test, y_train, y_test = train_test_split(x_poly, y, test_size = 0.2, random_state = 40)
     modelo = LinearRegression()
     modelo.fit(x_train, y_train)
     previsoes = modelo.predict(x_test)
     acuracia = r2_score(y_test, previsoes)
     mae = mean_absolute_error(y_test, previsoes)
     rmse = np.sqrt(mean_squared_error(y_test, previsoes))
     # calcula o módulo do erro e calcula-se a média(menos sensível a outliers)
     print(f'Erro médio absoluto (MAE): {mae:.2f}')# foca em erros médios típicos
     # calcula o erro de cada previsão, eleva ao quadrado e calcula a média, após isso calcula a raiz desse resultado para voltarmos para a unidade de medida original(diferenciavel, facilita o ajuste de parametros, penaliza o modelo pelos outliers)
     print(f'Erro médio quadrático (RMSE): {rmse:.2f}')# foca em erros grandes
     print(f"Acurácia (R²): {acuracia:.2%}")
     # Salva o modelo (os pesos da regressão)
     joblib.dump(modelo, 'modelo_polinomial.pkl')
     # Salva o transformador (as regras para criar Area², Area*Quartos, etc.)
     joblib.dump(poly, 'transformador_poly.pkl')
     limites_poly = [y_test.min(), y_test.max()]
     fig_poly = go.Figure()
     fig_poly.add_trace(go.Scatter(
     x= y_test, y=previsoes,
     mode='markers',
     marker=dict(color='royalblue', opacity=0.5),
     name='Previsão Polinomial'
     ))
     fig_poly.add_trace(go.Scatter(
     x=limites_poly, y=limites_poly,
     mode='lines',
     line=dict(color='black', dash='dash'),
     name='Ideal'
     ))
     fig_poly.update_layout(
     title=f'Regressão Polinomial)',
     xaxis_title='Preço Real',
     yaxis_title='Preço Previsto',
     template='plotly_white',
     width=700, height=500
     )
     fig_poly.update_xaxes(tickformat="$.2s")
     fig_poly.update_yaxes(tickformat="$.2s")
     fig_poly.show()     


def carregar_modelo():

     # 1. Carrega os arquivos binários de volta para a memória
     modelo_carregado = joblib.load('modelo_polinomial.pkl')
     poly_carregado = joblib.load('transformador_poly.pkl')

     # 2. Dados da nova casa (exatamente como no seu dataframe original)
     nova_casa = {
     'quartos': 3,
     'banheiros': 2.5,
     'area_construida_m2': 180,
     'andares': 2,
     'vista_agua': 0,
     'qualidade_vista': 0,
     'padrao_construcao': 7,
     'area_porao_m2': 0,
     'latitude': 47.5112,
     'area_construida_vizinhos_m2': 170,
     'idade_imovel' : 12,
     'proporcao_vizinhanca': 1,
     'densidade_banheiros': 0.80

     }

     # 3. Convertendo para DataFrame
     df_input = pd.DataFrame([nova_casa])

     # --- O PASSO MAIS IMPORTANTE ---
     # Transforma as 11 colunas originais em colunas polinomiais (ex: cria os quadrados e interações)
     # O modelo só aceita os dados se eles passarem por aqui primeiro
     df_input_poly = poly_carregado.transform(df_input)

     # 4. Fazer a previsão usando os dados transformados
     predicao = modelo_carregado.predict(df_input_poly)

     print(f"O preço estimado para este imóvel é: ${predicao[0]:,.2f}")







