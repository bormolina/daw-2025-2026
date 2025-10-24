import os
import sqlite3
from werkzeug.security import generate_password_hash

DB_PATH = os.environ.get("DB_PATH", "/data/app.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

db_existe = os.path.isfile(DB_PATH)

with sqlite3.connect(DB_PATH) as conn:
    if not db_existe:
        print(f"[create_db] Creando BD nueva en {DB_PATH}")
    else:
        print(f"[create_db] BD ya existe: {DB_PATH} (no se sobreescribe)")

    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT UNIQUE,
            password_hash TEXT,
            role TEXT
        );
    """)

    # Lista de usuarios iniciales
    usuarios = [
        ("admin", os.environ.get("ADMIN_PASSWORD", "Admin123!"), "admin"),
        ("paco", "Paco123!", "visor"),
        ("pepe", "Pepe123!", "agricultor"),
    ]

    for username, password, role in usuarios:
        cur = conn.execute("SELECT id FROM users WHERE username = ?", (username,))
        if not cur.fetchone():
            hash_ = generate_password_hash(password)
            conn.execute(
                "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                (username, hash_, role),
            )
            print(f"[create_db] Usuario '{username}' ({role}) creado.")
        else:
            print(f"[create_db] Usuario '{username}' ya existe, no se modifica.")

    conn.commit()