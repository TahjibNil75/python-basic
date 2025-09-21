from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional, Union


app = FastAPI()

class Coffe(BaseModel):
    id : int
    name : str
    origin : str

coffees : List[Coffe] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Coffee API"}


@app.get("/coffees")
def get_coffees():
    return coffees


@app.post("/coffees")
def add_coffees(coffee: Coffe):
    coffees.append(coffee)
    return coffee

@app.put("/coffees/{coffee_id}")
def update_coffee(coffee_id : int, updated_coffee: Coffe):
    for index, coffee in enumerate(coffees):
        if coffee.id == coffee_id:
            coffees[index] = updated_coffee
            return updated_coffee
    return {"error": "Coffee not found"}


@app.delete("/coffees/{coffee_id}")
def delete_coffee(coffee_id : int):
    for index, coffee in enumerate(coffees):
        if coffee.id == coffee_id:
            deleted_coffee = coffees.pop(index)
            return deleted_coffee
    return {"error": "Coffee not found"}


