import plotly.express as px



def plt_dist_preco(df):
    fig = px.histogram(df, x="preco", title = 'DISTRIBUIÇÃO DO PREÇO')
    fig.show()
    #sns.histplot(df['preco'], kde=True, bins=80, color= 'blue')
    #px.title('Distribuição da Coluna')
    #return px.show()

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

