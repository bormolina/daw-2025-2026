# Imagen base de Python ligera (versión 3.11, basada en Debian Slim)
FROM python:3.11-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# ----------------------------------------------------------
# Variables de entorno:
#  - PYTHONDONTWRITEBYTECODE=1 → evita generar archivos .pyc
#  - PYTHONUNBUFFERED=1 → desactiva el buffer de salida para logs en tiempo real
# ----------------------------------------------------------
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ----------------------------------------------------------
# Instalación de dependencias del sistema:
#  - Actualiza el índice de paquetes
#  - Instala certificados raíz para HTTPS (ca-certificates)
#  - Limpia la caché para reducir el tamaño final de la imagen
# ----------------------------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# ----------------------------------------------------------
# Copiamos el archivo de dependencias Python y las instalamos
#  --no-cache-dir → evita almacenar caché de pip
# ----------------------------------------------------------
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ----------------------------------------------------------
# Creamos el directorio /app/data (para persistir datos locales)
# y copiamos los archivos iniciales de la carpeta data del host
# ----------------------------------------------------------
RUN mkdir -p /app/data
COPY data /app/data

# ----------------------------------------------------------
# Copiamos el archivo principal de la aplicación (FastAPI)
# ----------------------------------------------------------
COPY app.py /app/app.py

# ----------------------------------------------------------
# Exponemos el puerto 8000 dentro del contenedor
# (aunque externamente podemos mapearlo al que queramos con docker-compose)
# ----------------------------------------------------------
EXPOSE 8000

# ----------------------------------------------------------
# Comando por defecto que ejecutará el servidor Uvicorn
# --host 0.0.0.0 → accesible desde fuera del contenedor
# --port 8000 → puerto interno del contenedor
# ----------------------------------------------------------
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]