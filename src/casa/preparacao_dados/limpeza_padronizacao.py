import pandas as pd
from pathlib import Path


def copiar_dataframe(df_velho):
    df_novo = df_velho.copy()
    return df_novo


def ler_arquivos(path):
    df = pd.read_csv(path)
    return df


def converter_para_data(df, coluna):
    df[coluna] = pd.to_datetime(df[coluna])
    return df


def converter_para_numero_e_m2(df, coluna = []):
    for cols in coluna:
     df[cols] = pd.to_numeric(df[cols], errors = 'coerce')
     df[cols] = df[cols] / 10.76389999
    return df


def verificar_minimos(df):
    colunas = df.select_dtypes(include = ['float64', 'int64']).columns
    return (df[colunas]).min()


def exportar_csv(df, nome,pasta):
  caminho = Path(pasta)
  caminho.mkdir(parents=True, exist_ok=True)
  caminho_total = caminho / nome
  return df.to_csv(caminho_total, index = False)
 
df = ler_arquivos('../data/df_casa.csv')
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
df_limpo = converter_para_data(df_limpo,'data')
df_limpo = converter_para_numero_e_m2(df_limpo, ['area_construida_ft2', 'area_terreno_ft2', 'area_acima_solo_ft2', 'area_porao_ft2', 'area_construida_vizinhos_ft2','area_terreno_vizinhos_ft2'])
df_limpo.rename(columns = {'area_construida_ft2': 'area_construida_m2',
                           'area_terreno_ft2': 'area_terreno_m2',
                           'area_acima_solo_ft2': 'area_acima_solo_m2',
                             'area_porao_ft2' : 'area_porao_m2',
                             'area_construida_vizinhos_ft2': 'area_construida_vizinhos_m2',
                              'area_terreno_vizinhos_ft2' : 'area_terreno_vizinhos_m2'
                              }, inplace = True) 
verificar_minimos(df_limpo)
exportar_csv(df_limpo, 'df_limpo.csv', '/home/lucas/Área de trabalho/projetos/projeto-preco-de-casas/src/casa/data')


