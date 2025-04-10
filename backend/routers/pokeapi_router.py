from fastapi import APIRouter
from fastapi import FastAPI, BackgroundTasks
import requests
import redis
import json
import time
from threading import Thread

import os
import random

app = FastAPI()
router = APIRouter()

redis_host = os.getenv("REDIS_HOST", "redis")  # Use Docker service name
redis_port = int(os.getenv("REDIS_PORT", 6379))
redis_client = redis.Redis(host=redis_host, port=redis_port, db=0, decode_responses=True)

UPDATE_INTERVAL = 30  # Fetch new data every 60 seconds


def fetch_and_store_data():
    while True:
        randNum = random.randint(1, 151)

        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{randNum}", timeout=5)

            if response.status_code == 200:
                print("\n200 RESPONSE\n")
                data = response.json()
                data = data['name']
                redis_client.set("latest_data", json.dumps(data))
            else:
                print(f"\nUnexpected status code: {response.status_code}\n")
                
        except requests.exceptions.ConnectionError:
            print("\nConnection Error...")
        except Exception as e:
            print(f"\nUnexpected error: {e}\n")
        
        time.sleep(UPDATE_INTERVAL)
        print("GETTING API DATA")


@router.on_event("startup")
def startup_event():
    Thread(target=fetch_and_store_data, daemon=True).start()


@router.get("/data")
def get_latest_data():
    data = redis_client.get("latest_data")
    return json.loads(data) if data else {"message": "No data available"}


@router.get("/something")
def something():
    return "somethingsomethingsomething"























