from fastapi import FastAPI
import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")

@app.get("/")
def home():
    return {"message": "SecureDevLab is running!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/users")
def get_users():
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, username, email FROM users")
            users = cursor.fetchall()

    return users