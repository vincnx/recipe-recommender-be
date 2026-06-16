FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    NLTK_DATA=/app/nltk_data \
    UV_LINK_MODE=copy \
    UV_PROJECT_ENVIRONMENT=/app/.venv

WORKDIR /app

RUN pip install --no-cache-dir uv==0.9.13

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev --no-install-project

COPY app.py ./
COPY src ./src

RUN mkdir -p /app/nltk_data \
 && uv run python -c "import nltk; nltk.download('punkt_tab', download_dir='/app/nltk_data')"

RUN groupadd --system app && useradd --system --gid app --home /app --shell /usr/sbin/nologin app \
 && chown -R app:app /app
USER app

EXPOSE 8080

CMD ["uv", "run", "gunicorn", \
     "--bind", "0.0.0.0:8080", \
     "--workers", "1", \
     "--timeout", "120", \
     "--access-logfile", "-", \
     "--error-logfile", "-", \
     "app:create_app()"]
