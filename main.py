from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from database import get_engine, Entry
from sqlmodel import Session

database_engine = get_engine()

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

    person = Entry(name=item.name, others=item.others, menu=item.menu, info=item.info)

    with Session(database_engine) as session:
        try:
            session.add(person)
            session.commit()
        except Exception as e:
            print(e)
            raise HTTPException(status_code=400, detail="Can't save item to database!")
            

