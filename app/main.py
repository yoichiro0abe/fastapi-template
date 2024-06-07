from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    import datetime

    now = datetime.datetime.now()
    return {"Hello": "World" if now.second % 5 != 0 else "bingo"}
    # return {"Hello": "World111"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
