from http import HTTPStatus

import requests
import streamlit as st

# Configuração da página
st.set_page_config(
    page_title='Preditor de Preço de Casas', page_icon='🏡', layout='wide'
)

API_URL = 'http://127.0.0.1:8000/predict'

st.title('Previsão de Preço de Imóveis')
st.write(
    'Preencha as características abaixo para obter uma estimativa do valor da casa.'
)

st.markdown('---')

# Criando formulário para organizar as entradas
with st.form('form_predicao'):
    st.subheader('Características Gerais do Imóvel')
    col1, col2, col3 = st.columns(3)

    with col1:
        quartos = st.number_input(
            'Número de Quartos', min_value=1, max_value=20, value=3, step=1
        )
        banheiros = st.number_input(
            'Número de Banheiros',
            min_value=0.5,
            max_value=10.0,
            value=2.0,
            step=0.5,
        )
        andares = st.number_input(
            'Número de Andares', min_value=1, max_value=5, value=1, step=1
        )

    with col2:
        area_construida_m2 = st.number_input(
            'Área Construída (m²)', min_value=10.0, value=120.0, step=5.0
        )
        area_porao_m2 = st.number_input(
            'Área do Porão (m²)', min_value=0.0, value=0.0, step=5.0
        )
        idade_imovel = st.number_input(
            'Idade do Imóvel (anos)', min_value=0.0, value=15.0, step=1.0
        )

    with col3:
        padrao_construcao = st.slider(
            'Padrão de Construção (1 a 13)', min_value=1, max_value=13, value=7
        )
        qualidade_vista = st.slider(
            'Qualidade da Vista (0 a 4)', min_value=0, max_value=4, value=0
        )
        vista_agua_opcao = st.radio(
            'Tem vista para água?', options=['Não', 'Sim'], horizontal=True
        )
        vista_agua = 1 if vista_agua_opcao == 'Sim' else 0

    st.subheader('Localização e Vizinhança')
    col4, col5 = st.columns(2)

    with col4:
        latitude = st.number_input('Latitude', value=47.5112, format='%.4f')

    with col5:
        area_construida_vizinhos_m2 = st.number_input(
            'Área Construída dos Vizinhos (m²)',
            min_value=10.0,
            value=110.0,
            step=5.0,
        )

    # CÁLCULOS AUTOMÁTICOS
    # Evita divisão por zero se o usuário colocar 0 em algum campo
    densidade_banheiros = banheiros / quartos if quartos > 0 else 0.0
    proporcao_vizinhanca = (
        area_construida_m2 / area_construida_vizinhos_m2
        if area_construida_vizinhos_m2 > 0
        else 0.0
    )

    # Exibe os valores calculados de forma informativa
    st.info(
        f'**Métricas calculadas automaticamente:** '
        f'Densidade de Banheiros: `{densidade_banheiros:.2f}` | '
        f'Proporção da Vizinhança: `{proporcao_vizinhanca:.2f}`'
    )

    # Botão de envio do formulário
    btn_submit = st.form_submit_button('Calcular Estimativa')

# PROCESSAMENTO DA REQUISIÇÃO
if btn_submit:
    dados_casa = {
        'quartos': quartos,
        'banheiros': banheiros,
        'area_construida_m2': area_construida_m2,
        'andares': andares,
        'vista_agua': vista_agua,
        'qualidade_vista': qualidade_vista,
        'padrao_construcao': padrao_construcao,
        'area_porao_m2': area_porao_m2,
        'latitude': latitude,
        'area_construida_vizinhos_m2': area_construida_vizinhos_m2,
        'idade_imovel': idade_imovel,
        'proporcao_vizinhanca': round(proporcao_vizinhanca, 4),
        'densidade_banheiros': round(densidade_banheiros, 4),
    }

    # 1. DENTRO DO TRY FICA APENAS A CHAMADA DA API
    try:
        with st.spinner('Conectando à API e realizando previsão...'):
            response = requests.post(API_URL, json=dados_casa)
    except requests.exceptions.ConnectionError:
        st.error(
            'Não foi possível conectar ao backend. '
            'Certifique-se de que a API FastAPI está rodando em http://127.0.0.1:8000'
        )
    # 2. O PROCESSAMENTO DA RESPOSTA VAI PARA O ELSE
    else:
        if (
            response.status_code == HTTPStatus.OK
        ):  # Substituído 200 por HTTPStatus.OK
            resultado = response.json()
            preco = resultado.get('preco_estimado', 0.0)

            st.success('Previsão realizada com sucesso!')
            st.metric(
                label='Preço Estimado do Imóvel', value=f'R$ {preco:,.2f}'
            )
        else:
            st.error(
                f'Erro na API (Status {response.status_code}): {response.text}'
            )
