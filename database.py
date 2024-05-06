from typing import Optional
from sqlmodel import Field, SQLModel



class Entry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: 
    age: Optional[int] = None

    name:str
    others: str
    accomodation: str
    menu: str
    info: str