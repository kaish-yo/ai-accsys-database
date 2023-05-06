from fastapi import Depends, FastAPI
from app.routers import auth, query
import logging
from .models import Base 
from .database import engine

Base.metadata.create_all(bind=engine, checkfirst=True) # if you want to narrow down the tables to create, use 'tables=[models.<Class>]

# initialize the app
app = FastAPI()

# app.include_router(auth.router)
app.include_router(query.router)

@app.get("/")
async def root():
    return {"message": "Hello world!"}