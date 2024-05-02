from typing import Union

from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()



class Item(BaseModel):
    name:str
    others: str
    accomodation: str
    menu: str
    info: str




@app.get("/")
async def read_root():
    return {"Nothing": "here"}


@app.post("/items/create")
async def save_item(item: Item):
    return {"item_name": item.name, "others": item.others, "accomodation": item.accomodation}