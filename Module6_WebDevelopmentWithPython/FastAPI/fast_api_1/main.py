from fastapi import FastAPI
from pydantic import BaseModel

from database import create_db_connection


class Item(BaseModel):
    name: str
    description: str


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    connection = create_db_connection()
    cursor = connection.cursor()

    insert_query = "INSERT INTO items (name, description) VALUES (%s, %s)"
    item_data = (item.name, item.description)
    cursor.execute(insert_query, item_data)

    connection.commit()
    connection.close()

    return {"message": "Item created successfully"} ,item_data
