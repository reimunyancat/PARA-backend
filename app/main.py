from fastapi import FastAPI, APIRouter
from routers import user, api

app = FastAPI()

router = APIRouter(prefix = "/user/external-data")
app.include_router(user.router)
app.include_router(api.router)

