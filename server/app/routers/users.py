from fastapi import APIRouter, HTTPException,Depends
from app.models.user import User
from app.models.address import Address
from app.models.profile import Profile
from app.database.connection import users_collection, addresses_collection, profiles_collection,get_db
from app.schema.schemas import list_user,list_user_id

from bson import ObjectId
from pymongo import MongoClient

router_user = APIRouter()

# Get Request Methods
@router_user.get("/")
async def get_user():
    users = list_user(users_collection.find())
    return users

@router_user.get("/{id}")
async def get_user_id(id: str):
    user = users_collection.find_one({"_id": ObjectId(id)})
    if user:
        return list_user_id([user])
    else:
        return {"message": "User not found"}