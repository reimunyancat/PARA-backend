from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel
from bson import ObjectId
from database import users_collection
from pymongo import MongoClient
from fastapi.encoders import jsonable_encoder
from dotenv import load_dotenv
import os

router = APIRouter(prefix="/user")

CLIENT = os.getenv("CLIENT")

client = MongoClient(CLIENT)
db = client["para5"]
print("db connected")

class User(BaseModel):
    id: str
    passwd: str

@router.post("/signup")
async def signup(user: User):
    if db['users'].find_one({"id": user.id}):
        raise HTTPException(status_code=400, detail="id already exists")

    db['users'].insert_one(jsonable_encoder(user))
    
    return {'status': 200, 'message': 'success'}

@router.post("/signin")
async def signin(user: User):
    if db['users'].find_one({"id": user.id, "pw": user.passwd}):
        return {'status': 200, 'message': 'success'}
    else:
        return {'status': 400, 'message': 'fail'}

@router.delete("/delete")
async def delete(user: User):
    if db['users'].find_one({"id": user.id, "pw": user.passwd}):
        db['users'].delete_one({"id": user.id, "pw": user.passwd})
        return {'status': 200, 'message': 'success'}
    else:
        return {'status': 400, 'message': 'fail'}