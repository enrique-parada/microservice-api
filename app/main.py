import string

from fastapi import FastAPI
from mangum import Mangum

from . import config
from .models import (
    AnalyzeTextRequest,
    AnalyzeTextResponse,
    AnalyzePasswordRequest,
    AnalyzePasswordResponse,
    InfoResponse,
)

app = FastAPI(
    title=config.SERVICE_NAME,
    version=config.VERSION,
    description="API sencilla para análisis de texto y passwords para la prueba DevOps",
)


@app.get("/health", tags=["system"])
def health_check():
    return {"status": "ok"}


@app.get("/info", response_model=InfoResponse, tags=["system"])
def service_info():
    return InfoResponse(
        service=config.SERVICE_NAME,
        version=config.VERSION,
        environment=config.APP_ENV,
    )


@app.post("/analyze", response_model=AnalyzeTextResponse, tags=["analyze"])
def analyze_text(payload: AnalyzeTextRequest):
    text = payload.text or ""
    has_numbers = any(ch.isdigit() for ch in text)
    has_uppercase = any(ch.isupper() for ch in text)

    return AnalyzeTextResponse(
        text=text,
        length=len(text),
        word_count=len(text.split()) if text else 0,
        has_numbers=has_numbers,
        has_uppercase=has_uppercase,
    )


@app.post(
    "/analyze/password",
    response_model=AnalyzePasswordResponse,
    tags=["analyze"],
)
def analyze_password(payload: AnalyzePasswordRequest):
    pwd = payload.password or ""

    has_numbers = any(ch.isdigit() for ch in pwd)
    has_uppercase = any(ch.isupper() for ch in pwd)
    special_chars = set(string.punctuation)
    has_special_chars = any(ch in special_chars for ch in pwd)

    score = 0
    if len(pwd) >= 8:
        score += 1
    if has_numbers:
        score += 1
    if has_uppercase:
        score += 1
    if has_special_chars:
        score += 1

    return AnalyzePasswordResponse(
        score=score,
        length=len(pwd),
        has_numbers=has_numbers,
        has_uppercase=has_uppercase,
        has_special_chars=has_special_chars,
    )

handler = Mangum(app)

