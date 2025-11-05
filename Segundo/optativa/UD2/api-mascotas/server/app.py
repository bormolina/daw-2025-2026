# FastAPI → framework principal para crear la API web
# HTTPException → permite devolver errores HTTP personalizados (404, 400, etc.)
# Query → facilita declarar y validar parámetros opcionales en las rutas (por ejemplo, ?category=perro)
from fastapi import FastAPI, Query

# CORSMiddleware → middleware que habilita CORS (Cross-Origin Resource Sharing)
from fastapi.middleware.cors import CORSMiddleware

# BaseModel → clase base de Pydantic usada para definir modelos de datos
# Permite validación automática y conversión de tipos al recibir/enviar JSON
from pydantic import BaseModel

# List, Optional → tipos genéricos de Python usados para anotar colecciones y valores opcionales
from typing import List, Optional

from datetime import datetime
from pathlib import Path

# json → módulo estándar para leer y escribir datos en formato JSON 
import json

app = FastAPI(title="Adopción de Mascotas", version="1.0.0")

# Permitir acceso desde cualquier origen (solo para desarrollo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------ Modelos ------------------
# No usar dataclass, no se llevan bien en general con los frameworks/bibliotecas/etc
class Pet(BaseModel):
    id: int
    name: str
    category: str  # p.ej. "perro", "gato"
    age: Optional[int] = None
    adopted: bool = False

class Message(BaseModel):
    pet_id: int
    name: str
    email: str
    message: Optional[str] = "Me gustaría adoptar esta mascota."

class MessageRecord(Message):
    id: int
    created_at: datetime

# ------------------ Simulamos una “BD” como una lista persistente ------------------
DB_PETS: List[Pet] = []
DB_MESSAGES: List[MessageRecord] = []
MESSAGE_SEQ = 1

# ------------------ Persistencia (JSON) ------------------
DATA_DIR = Path("data")
PETS_FILE = DATA_DIR / "pets.json"
MESSAGES_FILE = DATA_DIR / "messages.json"

# Crea la carpeta 'data' si no existe (para guardar los archivos JSON).
# El guion bajo indica que es una función interna, no pensada para ser usada fuera de este módulo.
def _ensure_data_dir():
    DATA_DIR.mkdir(exist_ok=True)

# Guarda la lista de mascotas (DB_PETS) en el archivo pets.json
def save_pets():
    _ensure_data_dir()
    with PETS_FILE.open("w", encoding="utf-8") as f:
        # Convierte cada objeto Pet en un diccionario con model_dump()
        # y lo guarda todo como una lista JSON legible.
        # ensure_ascii=False → permite tildes y eñes
        # indent=2 → deja sangrías para que el JSON sea más fácil de leer
        json.dump([p.model_dump() for p in DB_PETS], f, ensure_ascii=False, indent=2)

# Carga las mascotas desde pets.json o crea una semilla inicial si no existe
def load_pets():
    global DB_PETS
    if PETS_FILE.exists():
        with PETS_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
        # Crea un objeto Pet por cada diccionario del JSON.
        # El operador ** desempaqueta el diccionario como argumentos nombrados:
        # Pet(**{"id":1, "name":"Luna"}) equivale a Pet(id=1, name="Luna").
        DB_PETS = [Pet(**item) for item in data]
    else:
        # Semilla por defecto de mascotas iniciales si no existe el archivo.
        DB_PETS = [
            Pet(id=1, name="Luna",  category="gato",   age=2, adopted=False),
            Pet(id=2, name="Rocky", category="perro",  age=4, adopted=False),
            Pet(id=3, name="Kira",  category="perro",  age=1, adopted=True),
            Pet(id=4, name="Nube",  category="conejo", age=3, adopted=False),
            Pet(id=5, name="Mika",  category="gato",   age=5, adopted=False),
        ]
        save_pets()

# Guarda la lista de mensajes (DB_MESSAGES) en messages.json con la fecha formateada
def save_messages():
    pass

# Carga los mensajes desde messages.json o inicia una lista vacía si no existe
def load_messages():
    pass

# ------------------ Startup ------------------
@app.on_event("startup")
def _startup():
    load_pets()
    load_messages()

# ------------------ GETs ------------------

# Devuelve todas las mascotas o solo las de una categoría específica si se indica (?category=perro)
# # "Query(None, ...)" establece que su valor por defecto será None y añade descripción para la documentación automática.
@app.get("/pets/", response_model=List[Pet])
def list_pets(category: Optional[str] = Query(None, description="Filtra por categoría (perro, gato, etc.)")):
    if category is None:
        return DB_PETS
    cat = category.strip().lower()
    return [p for p in DB_PETS if p.category.lower() == cat]

# Devuelve una lista con los tipos de mascota existentes (sin duplicados)
@app.get("/types/", response_model=List[str])
def list_types():
    pass

# Devuelve todos los mensajes o solo los de una mascota concreta si se pasa pet_id
@app.get("/messages/", response_model=List[MessageRecord])
def list_messages(pet_id: Optional[int] = None):
    pass

# ------------------ PATCH ------------------

# Marca una mascota como adoptada, validando que exista y no lo esté ya
@app.patch("/pets/{pet_id}/adopt", response_model=Pet)
def adopt_pet(pet_id: int):
    pass
# ------------------ POSTs ------------------

# Registra un nuevo mensaje de adopción vinculado a una mascota existente
@app.post("/messages/", response_model=MessageRecord, status_code=201)
def create_message(msg: Message):
    pass