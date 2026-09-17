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

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "casa.backend.fastapi_zero.app:app", "--host", "0.0.0.0", "--port", "8000"]