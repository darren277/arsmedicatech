FROM python:3.12-slim AS base

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

COPY ./main.py ./main.py
ENV PYTHONPATH=/app

EXPOSE 5000

# ---------- runtime ----------
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
