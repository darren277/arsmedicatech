# ---------- build stage ----------
FROM python:3.12-slim as base

# system deps for spaCy CPU wheels
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

# Install everything in one layer to enable Docker cache
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download model so the image is self-contained
RUN python -m spacy validate

COPY app/ ./app
ENV PYTHONPATH=/app

# ---------- runtime ----------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
