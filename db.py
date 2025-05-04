import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def test_connection():
    try:
        conn = get_connection()
        cur = conn.cursor()
        print("✅ Conectado a la base de datos con éxito.")

        # Crear tabla si no existe
        cur.execute("""
            CREATE TABLE IF NOT EXISTS jugadores (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                position TEXT,
                genero TEXT,
                equipo TEXT
            );
        """)
        conn.commit()
        print("🛠️ Tabla 'jugadores' verificada o creada correctamente.")

        cur.close()
        conn.close()
    except Exception as e:
        print("❌ Error al conectar con la base de datos:")
        print(e)

if __name__ == "__main__":
    test_connection()

