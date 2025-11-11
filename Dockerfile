FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    build-essential \
    libpq-dev \
    gcc \
    curl \
    ca-certificates \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*


ENV UV_PROJECT_ENVIRONMENT=/opt/venv
ENV PATH="/opt/venv/bin:${PATH}"
 
COPY pyproject.toml uv.lock ./
 
RUN uv sync --locked

COPY . .

EXPOSE 8000

CMD ["sh", "-c", "\
  until nc -z db 5432; do sleep 1; done; \
  python manage.py migrate && \
  python manage.py collectstatic --noinput && \
  python manage.py runserver 0.0.0.0:8000 \
"]
