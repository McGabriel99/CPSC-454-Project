import sqlite3
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Application(BaseModel):
    student_id: int
    name: str
    status: str = "pending"  # Default to "pending" when created

# Initialize FastAPI app
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
def init_db():
    conn = sqlite3.connect('applications.db')
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS applications (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.get("/")
def read_root():
    return {"Hello": "World"}


# This endpoint expects a POST request with a 
# JSON body containing the student_id and name. 
# status is set to "pending" by default.
@app.post("/apply/")
def apply(application: Application):
    conn = sqlite3.connect('applications.db')
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO applications (student_id, name, status) VALUES (?, ?, ?)
    ''', (application.student_id, application.name, application.status))
    conn.commit()
    conn.close()
    return {"status": "application received", "data": application}


# checks the status attribute in the database for a specific user.
@app.get("/status/{student_id}")
def read_status(student_id: int):
    conn = sqlite3.connect('applications.db')
    cur = conn.cursor()
    cur.execute('SELECT status FROM applications WHERE student_id = ?', (student_id,))
    status = cur.fetchone()
    conn.close()
    if status:
        return {"student_id": student_id, "status": status[0]}
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# sets the status attribute to "withdrawn"
@app.post("/withdraw/{student_id}")
def withdraw(student_id: int):
    conn = sqlite3.connect('applications.db')
    cur = conn.cursor()
    cur.execute('''
        UPDATE applications SET status = 'withdrawn' WHERE student_id = ?
    ''', (student_id,))
    conn.commit()
    rows_affected = cur.rowcount
    conn.close()
    if rows_affected == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"student_id": student_id, "status": "withdrawn"}
