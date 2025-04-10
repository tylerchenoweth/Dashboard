import requests
import json
import random
import time
from utils.redis_client import redis_client

def fetch_and_store_data():

    UPDATE_INTERVAL = 30  # Fetch new data every 60 seconds
    
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

