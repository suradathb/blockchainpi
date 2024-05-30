# app/routers/address.py
from fastapi import APIRouter, HTTPException
from app.models.address import Address
from app.database import get_db

router = APIRouter()

@router.get("/addresses/{address_id}", response_model=Address)
async def get_address(address_id: str):
    db = get_db()
    address = db.get_address_by_id(address_id)
    if not address:
        raise HTTPException(status_code=404, detail="Address not found")
    return address

@router.post("/addresses/", response_model=Address)
async def create_address(address: Address):
    db = get_db()
    created_address = db.create_address(address)
    return created_address
