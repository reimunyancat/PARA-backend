from fastapi import APIRouter
from dotenv import load_dotenv
import requests
import os

router = APIRouter()
TOKEN = os.getenv("TOKEN")

@router.get("/external-data")
def get_external_data():
    response = requests.get(TOKEN)
    data = response.json()
    
    processed_data = [item['important_field'] for item in data]
    
    return {"processed_data": processed_data}