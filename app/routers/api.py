from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/external-data")
def get_external_data():
    response = requests.get('chat-gpt-temp')
    data = response.json()
    
    processed_data = [item['important_field'] for item in data]
    
    return {"processed_data": processed_data}
