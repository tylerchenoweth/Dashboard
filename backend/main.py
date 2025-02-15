from fastapi import FastAPI
from routers import pokeapi_router

app = FastAPI()

@app.get("/")
def first_example():
	return {"message": "hello, world! This is my dashboard app"}


app.include_router(pokeapi_router.router, prefix="/pokeapi", tags=["POKE API"])
