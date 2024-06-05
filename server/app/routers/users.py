from fastapi import APIRouter, HTTPException,Depends
from app.models.user import User
from app.models.address import Address
from app.models.profile import Profile
from app.database.connection import users_collection, addresses_collection, profiles_collection
from app.schema.schemas import list_user,list_user_id,list_address,list_profile,user_serial,address_serial,profile_serial
# from app.database.connection import get_db
from pymongo.database import Database

from bson import ObjectId
from pymongo import MongoClient

router_user = APIRouter()

# Get Request Methods
@router_user.get("/")
async def get_user():
    users = list_user(users_collection.find())
    return users

# @router_user.get("/{id}")
# async def get_user_id(id: str):
#     user = users_collection.find_one({"_id": ObjectId(id)})
#     address = addresses_collection.find_one({"user_id": user["_id"]})
#     print(address)
#     if user:
#         return list_user_id([user]) 
#     else:
#         return {"message": "User not found"}

@router_user.get("/{id}")
async def get_user_id(id: str):
    try:
        # ค้นหาผู้ใช้ตาม id
        user = users_collection.find_one({"_id": ObjectId(id)})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        # ดึงข้อมูลที่อยู่ทั้งหมดและพิมพ์เพื่อดีบัก
        all_addresses = list(addresses_collection.find())
        all_profiles= list(profiles_collection.find())
        print(all_profiles)
        # ค้นหาที่อยู่ตาม user_id โดยแปลง _id เป็น string และเปรียบเทียบกับค่าใน object ของ user_id
        address = addresses_collection.find_one({"user_id." + str(user["_id"]): str(user["_id"])})
        if not address:
            raise HTTPException(status_code=404, detail="Address not found for the user")
        
        profile = profiles_collection.find_one({"user_id." + str(user["_id"]): str(user["_id"])})
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found for the user")

        # แปลงผลลัพธ์เป็นรูปแบบที่ต้องการ
        user_info = user_serial(user)
        user_info['address'] = address_serial(address)  # เพิ่ม address ลงในข้อมูลผู้ใช้
        user_info['profile'] = profile_serial(profile)
        return user_info
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
@router_user.post("/login/")
async def login(username: str, password: str):
    existing_user = users_collection.find_one({"username": username})
    if existing_user and existing_user["password"] == password:
        return {"message": "Login successful", "user_id": str(existing_user["_id"])}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
        
@router_user.post("/register/")
async def register(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    user_dict = user.dict()
    user_id = users_collection.insert_one(user_dict).inserted_id
    return {"message": "User registered successfully", "user_id": str(user_id)}

