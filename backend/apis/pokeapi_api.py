import httpx
import numpy as np
import random
import redis
import json

# Connect to Redis (Change host/port if Redis is on another machine)
redis_client = redis.Redis(host="localhost", port=6379, db=0, decode_responses=True)

def cache_pokemon_data(key, data, expire=600):  # Default expiration is 10 minutes
    redis_client.setex(key, expire, json.dumps(data))

def get_cached_pokemon_data(key):
    cached_data = redis_client.get(key)
    return json.loads(cached_data) if cached_data else None

async def get_random_pokemon():
    """Fetches a random Pokémon with Redis caching"""
    randNum = random.randint(1, 151)
    cache_key = f"pokemon:random:{randNum}"  # Unique Redis key for each Pokémon

    # Check if data exists in Redis
    cached_data = get_cached_pokemon_data(cache_key)
    if cached_data:
        print(f"Cache HIT for {cache_key}")
        return cached_data  # Return cached data if available

    print(f"Cache MISS for {cache_key}. Fetching new data...")
    async with httpx.AsyncClient() as client:
        url = f"https://pokeapi.co/api/v2/pokemon/{randNum}"
        response = await client.get(url)
        data = response.json()

        # Store the response in Redis
        cache_pokemon_data(cache_key, data)
        print(f"Stored {cache_key} in Redis")
        return data

async def get_pokemon_by_id(pokemon_id):
    """Fetches a Pokémon by ID with Redis caching"""
    cache_key = f"pokemon:id:{pokemon_id}"  # Unique Redis key for each Pokémon

    # Check if data exists in Redis
    cached_data = get_cached_pokemon_data(cache_key)
    if cached_data:
        print(f"Cache HIT for {cache_key}")
        return cached_data  # Return cached data if available

    print(f"Cache MISS for {cache_key}. Fetching new data...")
    async with httpx.AsyncClient() as client:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
        response = await client.get(url)
        data = response.json()

        # Store the response in Redis
        cache_pokemon_data(cache_key, data)
        print(f"Stored {cache_key} in Redis")
        return data
