from http import HTTPStatus
from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException

from casa.backend.fastapi_zero.schemas import (
    EntradaCasa,
    Message,
    PredicaoPreco,
    UserDB,
    UserList,
    UserPublic,
    UserSchema,
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ML_DIR = BASE_DIR / 'analise_dados&ML' / 'machine_learning'
MODEL_PATH = Path(ML_DIR / 'modelo_polinomial.pkl')
MODEL_TRANSFORM_POLY = Path(ML_DIR / 'transformador_poly.pkl')
MODEL_SCALER = Path(ML_DIR / 'scaler.pkl')


database = []

app = FastAPI(title='API para previsao de preços de casas')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Ola mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)

    database.append(user_with_id)

    return user_with_id


@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {'users': database}


@app.put(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def update_user(user_id: int, user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=user_id)

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found!'
        )
    database[user_id - 1] = user_with_id

    return user_with_id


@app.delete(
    '/users/{user_id}', status_code=HTTPStatus.OK, response_model=UserPublic
)
def delete_user(user_id: int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail=' Not Found!'
        )
    return database.pop(user_id - 1)


@app.post('/predict', status_code=HTTPStatus.OK, response_model=PredicaoPreco)
def prever_preco(dados: EntradaCasa):

    # 1. Carrega os arquivos binários de volta para a memória
    modelo_carregado = joblib.load(MODEL_PATH)
    poly_carregado = joblib.load(MODEL_TRANSFORM_POLY)
    scaler_carregado = joblib.load(MODEL_SCALER)

    # 2. Convertendo para DataFrame
    df_input = pd.DataFrame([dados.model_dump()])

    df_input_scaled = scaler_carregado.transform(df_input)

    # --- O PASSO MAIS IMPORTANTE ---
    # Transforma as 11 colunas originais em colunas polinomiais (ex: cria os quadrados e interações)
    # O modelo só aceita os dados se eles passarem por aqui primeiro
    df_input_poly = poly_carregado.transform(df_input_scaled)

    # 4. Fazer a previsão usando os dados transformados
    predicao = modelo_carregado.predict(df_input_poly)

    return {'preco_estimado': round(float(predicao[0]), 2)}
