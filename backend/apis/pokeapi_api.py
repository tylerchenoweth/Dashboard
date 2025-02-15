import httpx
import numpy as np
import random

async def get_random_pokemon():

    async with httpx.AsyncClient() as client:
        randNum = int(np.round(random.random() * 151, decimals=0) + 1)
        url = f"https://pokeapi.co/api/v2/pokemon/{randNum}"

        response = await client.get(url)
        return response.json()

async def get_pokemon_by_id(pokemon_id):

    async with httpx.AsyncClient() as client:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"

        response = await client.get(url)
        return response.json()