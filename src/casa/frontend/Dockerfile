FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PYTHONPATH=/app/src

RUN pip install --no-cache-dir poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry install --no-root --without dev

COPY src /app/src

EXPOSE 8501

CMD ["poetry", "run", "streamlit", "run", "src/casa/frontend/app.py", "--server.port=8501", "--server.address=0.0.0.0"]