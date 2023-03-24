from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"lauris": "fghfdghfdghdfghdfghdfghfghdfgh"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"lauris": item_id, "q": q}