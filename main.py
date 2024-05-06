from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:3000",
]


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Item(BaseModel):
    name:str
    others: str
    menu: bool
    info: str




@app.get("/")
async def read_root():
    return {"Nothing": "here"}


@app.post("/items/create")
async def save_item(item: Item):
    return {"item_name": item.name, "others": item.others, "accomodation": item.accomodation}
