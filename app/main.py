from typing import Union
import os

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    import datetime

    now = datetime.datetime.now()
    api_key = os.getenv("API_KEY")
    return {"Hello": "World", "now": now, "api_key": api_key}
    # return {"Hello": "World111"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
