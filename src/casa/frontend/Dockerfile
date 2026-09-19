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
# Pego todo o meu código fonte e transfiro para o caminho app/src/casa/frontend dentro do container
COPY src/casa/frontend /app/src/casa/frontend
# Indica que a aplicação escuta na porta 8501
EXPOSE 8501
# Poetry run streamlit run (executo o streamlit com poetry) src/casa/frontend/app.py (cainho do arquivo contendo p código da minha interface) --server.port = 8501 (roda na porta 8501) --server.adress = 0.0.0.0( abro a rede do streamlit para aceitar conexões vindas de fora do container)
CMD ["poetry", "run", "streamlit", "run", "src/casa/frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]