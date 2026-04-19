import joblib
import pandas as pd
from casa.machine_learning.machine_learning import treinar_modelo
from casa.preparacao_dados.limpeza_padronizacao import ler_arquivos

df_deploy = ler_arquivos('../data/df_modelo.csv')
modelo_pronto,_,_,_,_,_, poly_treinado = treinar_modelo(df_deploy)

def salvar_modelo(modelo, poly):
    # Salva o modelo (os pesos da regressão)
    joblib.dump(modelo, 'modelo_polinomial.pkl')

    # Salva o transformador (as regras para criar Area², Area*Quartos, etc.)
    joblib.dump(poly, 'transformador_poly.pkl')

    print("Modelo e Transformador salvos com sucesso!")
    


salvar_modelo(modelo_pronto, poly_treinado)

def carregar_modelo():
 
# 1. Carrega os arquivos binários de volta para a memória
    modelo = joblib.load('modelo_polinomial.pkl')
    poly = joblib.load('transformador_poly.pkl')

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
        'idade_imovel': 2,
        'proporcao_vizinhanca': 1,
        'densidade_banheiros': 0.80

    }

    # 3. Convertendo para DataFrame
    df_input = pd.DataFrame([nova_casa])

    # --- O PASSO MAIS IMPORTANTE ---
    # Transforma as 11 colunas originais em colunas polinomiais (ex: cria os quadrados e interações)
    # O modelo só aceita os dados se eles passarem por aqui primeiro
    df_input_poly = poly.transform(df_input)

    # 4. Fazer a previsão usando os dados transformados
    predicao = modelo.predict(df_input_poly)

    print(f"O preço estimado para este imóvel é: ${predicao[0]:,.2f}")

carregar_modelo()