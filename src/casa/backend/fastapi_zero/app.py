from http import HTTPStatus
from pathlib import Path

import joblib
import pandas as pd
import torch
from fastapi import FastAPI
from casa.analise_dados_e_ml.machine_learning.model import RedeNeuralV2
from casa.backend.fastapi_zero.schemas import (
    EntradaCasa,
    PredicaoPreco,
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ML_DIR = BASE_DIR / 'analise_dados_e_ml' / 'machine_learning'
MODEL_PATH = Path(ML_DIR / 'champion_model.pth')
MODEL_SCALER = Path(ML_DIR / 'scaler.pkl')


app = FastAPI(title='API para previsao de preços de casas')


@app.post('/predict', status_code=HTTPStatus.OK, response_model=PredicaoPreco)
def prever_preco(dados: EntradaCasa):
    
    # weights_only = False para salvar o objeto completo
    modelo_carregado = RedeNeuralV2()
    modelo_carregado.load_state_dict(torch.load(f = MODEL_PATH, weights_only = True))
    modelo_carregado.eval()
    scaler_carregado = joblib.load(MODEL_SCALER)

    # JSON -> DICT -> DATAFRAME (dataframe pois o scaler precisa de um dataframe de entrada)
    df_input = pd.DataFrame([dados.model_dump()])

    df_input_scaled = scaler_carregado.transform(df_input)

    dados_tensor = torch.tensor(df_input_scaled.to_numpy(), dtype = torch.float32)

    with torch.inference_mode():
        predicao = modelo_carregado(dados_tensor)

    return {'preco_estimado': round(float(predicao[0]), 2)}
