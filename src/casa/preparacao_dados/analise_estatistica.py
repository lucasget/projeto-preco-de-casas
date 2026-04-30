import numpy as np
import plotly.express as px
from casa.preparacao_dados.limpeza_padronizacao import ler_arquivos, converter_para_data, exportar_csv

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


def plt_dist_preco(df):
    fig = px.histogram(df, x="preco", title = 'DISTRIBUIÇÃO DO PREÇO')
    fig.show()


def obter_e_plotar_medias_ano(df, ano):
    meses_pt = {
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril',
    5: 'Maio', 6: 'Junho', 7: 'Julho', 8: 'Agosto',
    9: 'Setembro', 10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
    }
    df['ano'] = df['data'].dt.year
    df_ano = df[df['ano'] == ano]
    df_ano['mes_num'] = df_ano['data'].dt.month
    df_ano['mes_nome'] = df_ano['mes_num'].map(meses_pt)
    medias_ano = df_ano.groupby(['mes_num','mes_nome'])['preco'].mean().reset_index() # analisar esse bloco
    medias_ano = medias_ano.sort_values('mes_num')
    fig = px.line(medias_ano, x = 'mes_nome',
               y = 'preco',
               title = f'Média de Preços de Casas por Mês (Ano {ano})',
               labels = {'mes_nome': 'MÊS', 'preco' : 'PREÇO MÉDIO (USD)'}, markers = True)
    fig.update_layout(font_family = "Times New Roman", title_font_family = "Courier New", xaxis = dict(tickmode = 'linear', tick0 = 1, dtick = 1))
    return fig.show()





df_estatistica = ler_arquivos('../data/df_limpo.csv')

converter_para_data(df_estatistica, 'data')

plt_dist_preco(df_estatistica)

obter_e_plotar_medias_ano(df_estatistica, 2014)

obter_e_plotar_medias_ano(df_estatistica, 2015)

plt_boxplot(df_estatistica, 'preco')

plt_dispersao(df_estatistica, 'area_construida_m2', 'preco')

analise_preco_longo_anos(df_estatistica)

df_estatistica = engenharia_atributos(df_estatistica)

calcular_correlacao(df_estatistica)


exportar_csv(df_estatistica, 'df_estatistica.csv', '/home/lucasb@rdt.local/Área de trabalho/Projetos/projeto-preco-de-casas/src/casa/data')




