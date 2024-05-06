from typing import Optional
from sqlmodel import Field, SQLModel, create_engine
import os

DB_USER = os.environ.get('PS_USER')
DB_PASS = os.environ.get('PS_PASS')

class Entry(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name:str
    others: str
    menu: bool
    info: str

connection_string = f"postgresql://{DB_USER}:{DB_PASS}@localhost:5432/wedding_people"

def get_engine():
    engine = create_engine(connection_string)
    return engine

engine = create_engine(connection_string)
SQLModel.metadata.create_all(engine)

