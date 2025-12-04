# PASO 1 — Instalar FastAPI y Uvicorn
# pip install fastapi uvicorn

# (Opcional: usar Docker con FastAPI + Uvicorn para practicar contenedores)

# PASO 2 — Crear carpeta y fichero .py
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

# PASO 3 — Instanciar la app
app = FastAPI(
    title="Adopción de Mascotas",
    version="1.0.0"
)

# PASO 4 — Modelo de datos
# Estoy haciendo una API para adoptar mascotas, especifico los campos de una mascota
class Pet(BaseModel):
    id: int
    name: str
    category: str
    age: Optional[int] = None
    adopted: bool = False


# PASO 5 — Endpoints de la API
# Es decir las llamadas de nuestra API
# Esta llamada devolvería todas las mascotas disponibles para adoptar
# Fíjate como especifico el método http: GET, POST, DELETE ...
@app.get("/pets/", response_model=List[Pet])
def get_pets():
    pass

# PASO 6 — Lanzar servidor
# uvicorn main:app --reload

# PASO 7 — Probar API en navegador:
# http://127.0.0.1:8000/pets/
# Documentación automática:
# http://127.0.0.1:8000/docs

# PASO 8 — (opcional) Consumir API desde un HTML con JS
"""
<script>
  async function cargar() {
    const r = await fetch("http://127.0.0.1:8000/pets/");
    const data = await r.json();
    console.log(data);  // Aquí ya tienes las mascotas
  }
  cargar();
</script>
""""""""""""