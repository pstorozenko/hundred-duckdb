from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# SQLite database filename
DATABASE_FILE = "data.sqlite"

# Create a connection to the database
conn = sqlite3.connect(DATABASE_FILE)

# # Create a table for answers if it doesn't exist
with conn:
    conn.execute("CREATE TABLE IF NOT EXISTS answers (id INTEGER PRIMARY KEY, answer VARCHAR)")

# Pydantic model for request body
class AnswerRequest(BaseModel):
    answer: str

# Endpoint to add a new answer
@app.post("/add_answer/")
def add_answer(answer: AnswerRequest):
    conn = sqlite3.connect(DATABASE_FILE)
    with conn:
        # Insert a new row into the table with the specified text
        cursor = conn.cursor()
        cursor.execute("INSERT INTO answers (answer) VALUES (?)", (answer.answer,))
        answer_id = cursor.lastrowid
        
    return {"id": answer_id, "answer": answer.answer}
