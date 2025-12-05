#!/usr/bin/env bash
set -e

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BUILD_DIR="$ROOT_DIR/build"
OUTPUT_ZIP="$ROOT_DIR/backend.zip"

echo "Limpiando build..."
rm -rf "$BUILD_DIR"
mkdir -p "$BUILD_DIR"

cd "$ROOT_DIR"

echo "Instalando dependencias en build/..."
pip install --upgrade pip >/dev/null
pip install -r requirements.txt -t "$BUILD_DIR" >/dev/null

echo "Copiando código de la app..."
cp -r app "$BUILD_DIR/"
cp main.py "$BUILD_DIR/"

echo "Creando ZIP..."
cd "$BUILD_DIR"
zip -r "$OUTPUT_ZIP" . >/dev/null

echo "✅ ZIP generado en: $OUTPUT_ZIP"

