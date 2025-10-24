#!/bin/sh
set -e # “Si cualquier comando de este script devuelve un error (código distinto de 0), detén la ejecución inmediatamente.”

echo "[entrypoint] Inicializando/verificando BD en ${DB_PATH}"
python /app/create_db.py

echo "[entrypoint] Lanzando Flask en 0.0.0.0:${FLASK_RUN_PORT}"
exec python /app/app.py