from fastapi import APIRouter
from apis import pokeapi_api
from fastapi import Path

import json, random, requests
import numpy as np

router = APIRouter()


def get_grams_to_lbs(weight):
    return round((weight / 4.53592), 2)


def format_data(data):

    # Extract and format the data
    context = {
        "name": data["name"].capitalize(),
        "image": data["sprites"]["front_default"],
        "order": data["id"],
        "type": data["types"][0]["type"]["name"], 
        "weight": get_grams_to_lbs( data["weight"] ),
        "gif": data["sprites"]["other"]["showdown"]["front_default"]
    }

    return context


@router.get("")
async def poke_api_home():
    return "Welcome to the PokeAPI routes!"


@router.get("/random")
async def get_pokeapi():
    
    data = await pokeapi_api.get_random_pokemon()  # Call the function from the API file
    context = format_data(data)

    return context


@router.get("/first_gen/{pokemon_id}")
async def get_pokemon_by_id(pokemon_id: int = Path(..., ge=1, le=151) ):

    data = await pokeapi_api.get_pokemon_by_id(pokemon_id)  # Call the function from the API file
    context = format_data(data)

    return context










































