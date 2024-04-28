from fastapi import FastAPI
from pydantic import BaseModel

class Application(BaseModel):
    student_id: int
    name: str
    status: str = "pending"  # Default to "pending" when created



app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/apply/")
def apply(application: Application):
    # This is a placeholder for database interaction
    return {"status": "application received", "data": application}

@app.get("/status/{student_id}")
def read_status(student_id: int):
    # Placeholder for fetching data from the database
    return {"student_id": student_id, "status": "pending"}

@app.post("/withdraw/{student_id}")
def withdraw(student_id: int):
    # Placeholder to update status in the database
    return {"student_id": student_id, "status": "withdrawn"}
