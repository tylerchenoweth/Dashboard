from fastapi import FastAPI
from routers import pokeapi_router

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow requests from your frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def first_example():
	return {"message": "hello, world! This is my dashboard app"}


app.include_router(pokeapi_router.router, prefix="/pokeapi", tags=["POKE API"])
