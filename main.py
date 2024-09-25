from fastapi import FastAPI, Depends, HTTPException
from database import engine
from sqlalchemy.orm import Session
from models import Base
from database import get_db
import crud, schemas

#init FastAPI app
app = FastAPI()

#Create db table
Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"message": "This is Task Manager API"}

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
   return crud.create_user(db=db, user=user)


@app.post("/tasks/", response_model=schemas.Task)
def create_user(task: schemas.TaskCreate, db: Session = Depends(get_db), user_id: int = 1):
   return crud.create_task(db=db, user=user, user_id=user_id)
