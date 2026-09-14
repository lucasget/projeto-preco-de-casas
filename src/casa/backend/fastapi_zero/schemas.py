from pydantic import BaseModel, Field


class EntradaCasa(BaseModel):
    quartos: int = Field(description='Numero de quartos')
    banheiros: float = Field(description='Numero de banheiros')
    area_construida_m2: float = Field(
        description='Tamanho da area construida do terreno em m2'
    )
    andares: int = Field(description='Numero andares da casa')
    vista_agua: int = Field(
        description='0 se nao tem vista para agua e 1 se tiver'
    )
    qualidade_vista: int = Field(description='Qualidade da casa(mar,rio, etc)')
    padrao_construcao: int = Field(description='Padrao da construçao')
    area_porao_m2: float = Field(description='Area do porao da casa')
    latitude: float = Field(description='Latitude da localizaçao da casa')
    area_construida_vizinhos_m2: float = Field(
        description='Area da casa construida do vizinho'
    )
    idade_imovel: float = Field(description=' quantos anos tem o imovel?')
    proporcao_vizinhanca: float = Field(
        description='area construida da sua casa / area construida da casa do vizinho'
    )
    densidade_banheiros: float = Field(
        description='Numero de banheiros / numero de quartos'
    )


class PredicaoPreco(BaseModel):
    preco_estimado: float
