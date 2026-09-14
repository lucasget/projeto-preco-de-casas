from http import HTTPStatus


# Verifica se a API retorna o PredicaoPreco corretamente
def test_prever_preco_com_sucesso(client):
    # Arrange: Conjunto de dados válido com todos os campos de EntradaCasa
    payload_valido = {
        "quartos": 3,
        "banheiros": 2.0,
        "area_construida_m2": 120.0,
        "andares": 1,
        "vista_agua": 0,
        "qualidade_vista": 0,
        "padrao_construcao": 7,
        "area_porao_m2": 0.0,
        "latitude": 47.5112,
        "area_construida_vizinhos_m2": 110.0,
        "idade_imovel": 15.0,
        "proporcao_vizinhanca": 1.09,
        "densidade_banheiros": 0.67,
    }

    # Act: Faz a requisição POST
    response = client.post('/predict', json=payload_valido)

    # Assert:
    # O código de status deve ser OK
    assert response.status_code == HTTPStatus.OK

    dados = response.json()

    # A chave esperada do PredicaoPreco deve estar no dicionário
    assert 'preco_estimado' in dados

    # O tipo retornado deve ser um float
    assert isinstance(dados['preco_estimado'], float)