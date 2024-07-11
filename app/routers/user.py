from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from bson import ObjectId
from database import users_collection

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

@router.post("/register")
def register_user(user: User):
    if users_collection.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already registered")
    
    user_dict = user.dict()
    users_collection.insert_one(user_dict)
    return {"message": "User registered successfully"}

@router.post("/login")
def login_user(user: User):
    existing_user = users_collection.find_one({"username": user.username, "password": user.password})
    if existing_user:
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@router.delete("/delete/{user_id}")
def delete_user(user_id: str):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="User not found")
