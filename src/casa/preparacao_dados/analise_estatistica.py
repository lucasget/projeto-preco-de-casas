import numpy as np
import plotly.express as px

def plt_boxplot(df, coluna):
    fig = px.box(df, y = coluna, title = f'Boxplot Interativo de {coluna}')
    fig.show()
def plt_dispersao(df, x , y):
    fig = px.scatter(df, x = x, y = y, title = f'Gráfico de dispersão({x} x {y})')
    fig.show()
def analise_preco_longo_anos (df):
    analise_anual = df.groupby('ano_construcao')['preco'].agg(['mean', 'std']).reset_index()
    analise_anual.columns = ['ano_construcao', 'preco_medio', 'desvio_padrao']
    analise_anual = analise_anual.sort_values('ano_construcao')
    fig_anual = px.line(analise_anual, x = 'ano_construcao', y = 'preco_medio', title = 'Analise do preço ao longo dos anos', labels = {'ano_construcao': 'Ano de Construção', 'preco_medio': 'Preço Médio(R$)'}, hover_data = {'desvio_padrao': ':,.2f'}, markers = True) 
    fig_anual.show()
def calcular_correlacao(df):
    return print(df.corr())


def engenharia_atributos(df):
    df['idade_imovel'] = df['ano'] - df['ano_construcao']
    df['proporcao_vizinhanca'] = df['area_construida_m2']/ df['area_construida_vizinhos_m2']
    df['densidade_banheiros'] = df['banheiros'] / df['quartos']
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna()
    return df




