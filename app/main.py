from fastapi import FastAPI

from app.database.database import engine, Base
from app.models.student import Student
from app.routes.students import router as student_router


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Student Database Management System",
    description="Backend API for managing student information",
    version="1.0.0"
)


app.include_router(student_router)


@app.get("/")
def home():
    return {"message": "Student Database API is running!"}