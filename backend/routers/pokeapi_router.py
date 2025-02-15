from fastapi import APIRouter
from apis import pokeapi_api
from fastapi import Path

import json, random, requests
import numpy as np

router = APIRouter()


def format_data(data):

    # Extract and format the data
    context = {
        "name": data["name"].capitalize(),
        "image": data["sprites"]["front_default"],
        "order": data["id"],
        "type": data["types"][0]["type"]["name"], 
        "weight": data["weight"],
        "gif": data["sprites"]["other"]["showdown"]["front_default"]
    }

    return context



@router.get("")
async def get_pokeapi():
 
    data = await pokeapi_api.get_random_pokemon()  # Call the function from the API file
    context = format_data(data)

    return context


@router.get("/first_gen/{pokemon_id}")
async def get_pokeapi(pokemon_id: int = Path(..., ge=1, le=151) ):

    data = await pokeapi_api.get_pokemon_by_id(pokemon_id)  # Call the function from the API file
    context = format_data(data)

    return context