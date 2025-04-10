from fastapi import APIRouter
from fastapi import FastAPI, BackgroundTasks
import requests
import json

from threading import Thread


from services.pokeapi_service import fetch_and_store_data
from utils.redis_client import redis_client

app = FastAPI()
router = APIRouter()


@router.on_event("startup")
def startup_event():
    Thread(target=fetch_and_store_data, daemon=True).start()


@router.get("/randomoriginal")
def get_latest_data():
    data = redis_client.get("latest_data")
    return json.loads(data) if data else {"message": "No data available"}


@router.get("/something")
def something():
    return "somethingsomethingsomething"























