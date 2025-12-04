from pydantic import BaseModel


class AnalyzeTextRequest(BaseModel):
    text: str


class AnalyzeTextResponse(BaseModel):
    text: str
    length: int
    word_count: int
    has_numbers: bool
    has_uppercase: bool


class AnalyzePasswordRequest(BaseModel):
    password: str


class AnalyzePasswordResponse(BaseModel):
    score: int
    length: int
    has_numbers: bool
    has_uppercase: bool
    has_special_chars: bool


class InfoResponse(BaseModel):
    service: str
    version: str
    environment: str

