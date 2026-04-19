import time
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from casa.preparacao_dados.limpeza_padronizacao import ler_arquivos
from casa.preparacao_dados.limpeza_padronizacao import exportar_csv
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error


#calcular_correlacao(df_modelo)
def plot_todas_distribuicoes(df):
     sns.pairplot(df, diag_kind='kde')
     plt.show()


"""def treinar_e_plotar_modelo(df):
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
     fig_poly.show()  """   


def treinar_modelo(df):
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
     return modelo, previsoes, y_test, x_train, y_train, x_test, poly



def plt_modelo(previsoes,y_test):

# 1. Pegando os dados da Célula 4 (Polinomial)
# 'previsoes' já contém os resultados do modelo polinomial
     limites_poly = [y_test.min(), y_test.max()]

# 2. Criar a figura
     fig_poly = go.Figure()

# Pontos de previsão
     fig_poly.add_trace(go.Scatter(
          x=y_test, y=previsoes,
          mode='markers',
          marker=dict(color='royalblue', opacity=0.5),
          name='Previsão Polinomial'
     ))

# Linha de Acerto Perfeito
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

if __name__ == "__main__" :
     df_modelo = ler_arquivos('/home/lucas/Área de trabalho/projetos/projeto-preco-de-casas/src/casa/data/df_estatistica.csv')



     colunas_excluir = ['id_imovel', 'data', 'area_terreno_m2', 
                   'condicao_imovel', 'ano_construcao', 'ano_reforma',
                   'cep', 'longitude', 'area_terreno_vizinhos_m2', 'ano', 'area_acima_solo_m2']


     df_modelo = df_modelo.drop(columns = colunas_excluir)

     #plot_todas_distribuicoes(df_modelo)

     modelo, p,y_test,x_train,y_train,x_test, po = treinar_modelo(df_modelo)



     plt_modelo(p,y_test)


     exportar_csv(df_modelo, 'df_modelo.csv','/home/lucas/Área de trabalho/projetos/projeto-preco-de-casas/src/casa/data')



