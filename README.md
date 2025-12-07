# microservice-api – DevOps Text Toolkit (Backend)

Backend de ejemplo construido con **FastAPI** y empaquetado para correr como **AWS Lambda** detrás de **API Gateway HTTP**.
Expone una pequeña API de análisis de texto y contraseñas que sirve como base para demostrar:

- Buenas prácticas de **GitFlow**.
- **CI/CD** con GitHub Actions (tests, linting y seguridad).
- Despliegue **serverless** orquestado con Terraform.

---

##  Funcionalidad

La API ofrece cuatro endpoints principales:

- `GET /health`
  Verifica que el servicio está vivo.

- `GET /info`
  Devuelve metadatos del servicio (nombre, versión, entorno).

- `POST /analyze`
  Recibe un texto y devuelve métricas básicas (longitud, número de palabras, flags).

- `POST /analyze/password`
  Recibe una contraseña y devuelve un “score” junto con validaciones simples (longitud, números, mayúsculas, caracteres especiales).

Esta API es consumida por el frontend (`microservice-frontend`) desplegado en S3.

---

## Stack técnico

- **Lenguaje:** Python 3.12
- **Framework web:** FastAPI
- **Serverless adapter:** Mangum (FastAPI → Lambda)
- **Modelado de datos:** Pydantic
- **Tests:** pytest
- **CI:** GitHub Actions
- **Infra (no en este repo):** Terraform (`infra-terraform`)
- **Empaquetado Lambda:** ZIP generado por script (`scripts/build_lambda_zip.sh`)

---

## Estructura del proyecto

```text
microservice-api/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI app + rutas + handler Mangum
│   ├── config.py        # Configuración básica (APP_ENV, etc.)
│   └── models.py        # Modelos Pydantic de requests/responses
├── main.py              # Bridge para Lambda (reexporta handler)
├── tests/
│   └── test_main.py     # Tests de endpoints principales
├── scripts/
│   └── build_lambda_zip.sh  # Script para empaquetar Lambda
├── requirements.txt
├── requirements-dev.txt     # ruff, bandit, etc.
├── README.md
└── .github/
    └── workflows/
        └── ci.yml       # CI: tests + lint + seguridad
```

## Ejecutar en local

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
API disponible en http://127.0.0.1:8000 (docs en /docs).

## Tests

```bash
pytest -v
```
