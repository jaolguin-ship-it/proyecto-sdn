#!/bin/bash
echo "--- Iniciando proceso de automatizacion Docker ---"
echo "1. Construyendo la imagen..."
docker build -t app-mindicador .
echo "2. Limpiando contenedores antiguos si existen..."
docker rm -f samplerunning 2>/dev/null
echo "3. Ejecutando el contenedor..."
docker run --name samplerunning -e API_URL_PROYECTO="https://mindicador.cl/api" app-mindicador
echo "--- Proceso finalizado con exito ---"