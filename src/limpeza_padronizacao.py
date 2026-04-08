import pandas as pd

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


def exportar_csv(df, nome):
    return df.to_csv(nome, index = False)




