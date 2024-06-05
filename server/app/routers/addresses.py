# app/routers/address.py
from fastapi import APIRouter, HTTPException
from app.models.address import Address
from app.database.connection import addresses_collection
from app.schema.schemas import list_address
from bson import ObjectId

router_address = APIRouter()

@router_address.get("/addresses")
async def get_address():
    address = list_address(addresses_collection.find())
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

@router_address.get("/{user_id}")
async def get_user_id(user_id: str):
    address = addresses_collection.find_one({"user_id": user_id})
    if address:
        return list_address([address])
    else:
        return {"message": "address not found"}


@router_address.post("/address/")
async def add_address(address: Address):
    address_dict = address.dict()
    address_id = addresses_collection.insert_one(address_dict).inserted_id
    return {"message": "Address added successfully", "address_id": str(address_id)}
