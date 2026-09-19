# Imagem base oficial do python na versão reduzida
FROM python:3.12-slim
# Variaveis de ambiente
# Desativa o buffer de saida do Python, forçando o envio imediato dos logs diretamente para o terminal
ENV PYTHONUNBUFFERED=1 \
    # Não deixa o poetry criar uma venv separada dentro do docker
    POETRY_VIRTUALENVS_CREATE=false \
    # Coloca src no caminho de busca do python, quando for importar não preciso colocar o src. nos imports
    PYTHONPATH=/app/src
# Instala as ferramentas do poetry(--no-cache-dir é para não guardar uma cópia do arquivo de instalação em uma pasta temporária de cache) 
RUN pip install --no-cache-dir poetry
# Cria e estabelece a pasta /app como o diretório de trabalho padrão dentro do container, todos os comandos que vierem depois serão executados a partir desse caminho
WORKDIR /app
# Copia os arquivos das dependências do projeto para a pasta( o * torna o arquivo opcional(nao usei nesse caso))
COPY pyproject.toml poetry.lock /app/
# Instalo as dependencias sem a parte dev e sem "instalar" o meu próprio código
RUN poetry install --no-root --without dev
# Pego todo o meu código fonte e transfiro para o caminho app/src/casa/backend dentro do container
COPY src/casa/backend/fastapi_zero /app/src/casa/backend
# Indica que a aplicação escuta na porta 8000
EXPOSE 8000
# Poetry run uvicorn (inicia o servidor com poetry) casa.backend.fastapi_zero.app:app (localiza o arquivo app.py) --host 0.0.0.0 (faz a aplicação escutar em todas as interfaces da rede do container) --port 8000 ( escuta as requisições na porta 8000) 
CMD ["poetry", "run", "uvicorn", "casa.backend.fastapi_zero.app:app", "--host", "0.0.0.0", "--port", "8000"]