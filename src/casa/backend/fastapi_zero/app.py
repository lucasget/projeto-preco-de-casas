from http import HTTPStatus
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI

from casa.backend.fastapi_zero.schemas import (
    EntradaCasa,
    PredicaoPreco,
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ML_DIR = BASE_DIR / 'analise_dados&ML' / 'machine_learning'
MODEL_PATH = Path(ML_DIR / 'champion_model.pkl')
MODEL_SCALER = Path(ML_DIR / 'scaler.pkl')


app = FastAPI(title='API para previsao de preços de casas')


@app.post('/predict', status_code=HTTPStatus.OK, response_model=PredicaoPreco)
def prever_preco(dados: EntradaCasa):

    modelo_carregado = joblib.load(MODEL_PATH)
    scaler_carregado = joblib.load(MODEL_SCALER)

    # Convertendo para DataFrame
    df_input = pd.DataFrame([dados.model_dump()])

    df_input_scaled = scaler_carregado.transform(df_input)


    predicao = modelo_carregado.predict(df_input_scaled)

    return {'preco_estimado': round(float(predicao[0]), 2)}
