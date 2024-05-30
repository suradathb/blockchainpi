from fastapi import APIRouter
from app.models.todos import Todo
from app.database.connection import collection_name
from app.schema.schemas import list_serial
from bson import ObjectId

router = APIRouter()

# Get Request Methods
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos

# POST Request Methods
@router.post("/")
async def post_todos(todo: Todo):
    collection_name.insert_one(dict(todo))
    return {"message": "Todo item added successfully"}

# PUT Request Methods
@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return {"message": "Todo item updated successfully"}

# DELETE Request Methods
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "Todo item deleted successfully"}