# from fastapi import APIRouter
# from apis import pokeapi_api
# from fastapi import Path

# import json, random, requests
# import numpy as np

# router = APIRouter()


# def get_grams_to_lbs(weight):
#     return round((weight / 4.53592), 2)


# def format_data(data):

#     # Extract and format the data
#     context = {
#         "name": data["name"].capitalize(),
#         "image": data["sprites"]["front_default"],
#         "order": data["id"],
#         "type": data["types"][0]["type"]["name"], 
#         "weight": get_grams_to_lbs( data["weight"] ),
#         "gif": data["sprites"]["other"]["showdown"]["front_default"]
#     }

#     return context


# @router.get("")
# async def poke_api_home():
#     return "Welcome to the PokeAPI routes!"


# @router.get("/random")
# async def get_pokeapi():
    
#     data = await pokeapi_api.get_random_pokemon()  # Call the function from the API file
#     context = format_data(data)

#     return context


# @router.get("/first_gen/{pokemon_id}")
# async def get_pokemon_by_id(pokemon_id: int = Path(..., ge=1, le=151) ):

#     data = await pokeapi_api.get_pokemon_by_id(pokemon_id)  # Call the function from the API file
#     context = format_data(data)

#     return context













from fastapi import APIRouter
from fastapi import FastAPI, BackgroundTasks
import requests
import redis
import json
import time
from threading import Thread

app = FastAPI()
router = APIRouter()
redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

API_URL = "https://api.example.com/data"
UPDATE_INTERVAL = 60  # Fetch new data every 60 seconds







# url = f"https://pokeapi.co/api/v2/pokemon/{randNum}"
# response = await client.get(url)
# data = response.json()

# return data

import random




def fetch_and_store_data():
    while True:
        randNum = random.randint(1, 151)
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{randNum}")
        
        if response.status_code == 200:
            data = response.json()
            data = data['name']
            redis_client.set("latest_data", json.dumps(data))
        time.sleep(UPDATE_INTERVAL)
        print("GETTING API DATA")

@router.on_event("startup")
def startup_event():
    Thread(target=fetch_and_store_data, daemon=True).start()

@router.get("/data")
def get_latest_data():
    data = redis_client.get("latest_data")
    return json.loads(data) if data else {"message": "No data available"}


























