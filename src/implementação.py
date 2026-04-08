import matplotlib
from limpeza_padronizacao import ler_arquivos
from limpeza_padronizacao import copiar_dataframe
from limpeza_padronizacao import converter_para_data
from limpeza_padronizacao import verificar_minimos
from limpeza_padronizacao import converter_para_numero_e_m2
from limpeza_padronizacao import exportar_csv
from consultas_agregacoes import obter_e_plotar_medias_ano
from consultas_agregacoes import plt_dist_preco
from analise_estatistica import plt_boxplot
from analise_estatistica import plt_dispersao
from analise_estatistica import analise_preco_longo_anos
from analise_estatistica import engenharia_atributos
from analise_estatistica import calcular_correlacao
from machine_learning import treinar_e_plotar_modelo
from machine_learning import carregar_modelo

matplotlib.use('TkAgg')
#LIMPEZA E PADRONIZAÇÃO
df = ler_arquivos('df_casa.csv')
df_limpo = copiar_dataframe(df)
df_limpo = df_limpo.rename(columns={
    'id': 'id_imovel',
    'date': 'data',
    'price': 'preco',
    'bedrooms': 'quartos',
    'bathrooms': 'banheiros',
    'sqft_living': 'area_construida_ft2',
    'sqft_above': 'area_acima_solo_ft2',
    'sqft_basement': 'area_porao_ft2',
    'sqft_lot': 'area_terreno_ft2',
    'floors': 'andares',
    'waterfront': 'vista_agua',
    'view': 'qualidade_vista',
    'grade': 'padrao_construcao',
    'condition': 'condicao_imovel',
    'yr_built': 'ano_construcao',
    'yr_renovated': 'ano_reforma',
    'zipcode': 'cep',
    'lat': 'latitude',
    'long': 'longitude',
    'sqft_living15': 'area_construida_vizinhos_ft2',
    'sqft_lot15': 'area_terreno_vizinhos_ft2'
})
df_limpo = converter_para_data(df_limpo, 'data')
verificar_minimos(df_limpo)
df_limpo.columns
converter_para_numero_e_m2(df_limpo, ['area_construida_ft2', 'area_terreno_ft2', 'area_acima_solo_ft2', 'area_porao_ft2', 'area_construida_vizinhos_ft2','area_terreno_vizinhos_ft2'])
df_limpo.rename(columns = {'area_construida_ft2': 'area_construida_m2',
                           'area_terreno_ft2': 'area_terreno_m2',
                           'area_acima_solo_ft2': 'area_acima_solo_m2',
                             'area_porao_ft2' : 'area_porao_m2',
                             'area_construida_vizinhos_ft2': 'area_construida_vizinhos_m2',
                              'area_terreno_vizinhos_ft2' : 'area_terreno_vizinhos_m2'
                              }, inplace = True)
verificar_minimos(df_limpo)
exportar_csv(df_limpo, 'df_limpo.csv')

#CONSULTAS E AGREGAÇÕES
df_consulta = ler_arquivos('df_limpo.csv')
df_consulta = converter_para_data(df_consulta, 'data')
obter_e_plotar_medias_ano(df_consulta, 2014)
obter_e_plotar_medias_ano(df_consulta, 2015)
plt_dist_preco(df_consulta)
exportar_csv(df_consulta, 'df_consulta.csv')

#ANALISE ESTATÍSTICA
df_estatistica = ler_arquivos('df_consulta.csv')
converter_para_data(df_estatistica, 'data')
plt_boxplot(df_estatistica, 'preco')
plt_dispersao(df_estatistica, 'area_construida_m2', 'preco')
analise_preco_longo_anos(df_estatistica)
df_estatistica = engenharia_atributos(df_estatistica)
calcular_correlacao(df_estatistica)
df_estatistica.isnull()
exportar_csv(df_estatistica, 'df_estatistica.csv')

#MACHINE LEARNING E DEPLOY
df_modelo = ler_arquivos('df_estatistica.csv')
df_modelo = converter_para_data(df_modelo, 'data')
df_modelo = df_modelo.dropna()
colunas_excluir = ['id_imovel', 'data', 'area_terreno_m2', 
                    'condicao_imovel', 'ano_construcao', 'ano_reforma',
                    'cep', 'longitude', 'area_terreno_vizinhos_m2', 'ano', 'area_acima_solo_m2']
df_modelo = df_modelo.drop(columns = colunas_excluir)
treinar_e_plotar_modelo(df_modelo)
carregar_modelo()







