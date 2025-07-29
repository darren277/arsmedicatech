"""
A simple FastAPI app for extracting named entities from text using spaCy.
"""
import os
from fastapi import FastAPI
from pydantic import BaseModel
import spacy, logging, subprocess, sys

#MODEL = "en_core_sci_sm"   # swap for _md, _lg or _scibert if you wish
MODEL = os.environ.get("MODEL_NAME", "en_core_web_sm")  # default to small English model
PIPE_DISABLE = ["parser", "lemmatizer"]  # we only need NER

import time
print("Starting load...")
t0 = time.time()

# Lazy-load with download fallback (useful for local dev runs)
try:
    nlp = spacy.load(MODEL, disable=PIPE_DISABLE)
except OSError:
    logging.warning(f"{MODEL} not found – downloading...")
    subprocess.run([sys.executable, "-m", "spacy", "download", MODEL], check=True)
    nlp = spacy.load(MODEL, disable=PIPE_DISABLE)

print(f"Model loaded in {time.time() - t0:.2f} seconds")

app = FastAPI(title="Concept Extraction API", version="0.1.0")


class TextIn(BaseModel):
    text: str


class EntityOut(BaseModel):
    text: str
    label: str
    start_char: int
    end_char: int


class ExtractionOut(BaseModel):
    entities: list[EntityOut]


@app.post("/ner/extract", response_model=ExtractionOut)
async def extract(payload: TextIn) -> ExtractionOut:
    """
    Extract named entities from the provided text.
    """
    doc = nlp(payload.text)
    ents = [
        EntityOut(
            text=e.text,
            label=e.label_,
            start_char=e.start_char,
            end_char=e.end_char,
        )
        for e in doc.ents
    ]
    return ExtractionOut(entities=ents)


@app.get("/ner/ready")
async def ready() -> dict:
    """
    Check if the service is ready.
    """
    return {"status": "ready", "model": MODEL}
