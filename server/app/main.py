from fastapi import FastAPI,HTTPException
from app.routers.route import router as todo_router
from app.routers.product import product as product_router
from app.database.connection import users_collection, addresses_collection, profiles_collection
from app.models.user import User
from app.models.address import Address
from app.models.profile import Profile
from app.routers.route import router as todo_router
from app.routers.product import product as product_router
from app.routers.users import router_user as user_router
from bson import ObjectId


app = FastAPI()

app.include_router(todo_router, prefix="/todos", tags=["Todos"])
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(user_router, prefix="/users", tags=["Users"])


from pymongo import MongoClient
@app.post("/register/")
async def register(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    user_dict = user.dict()
    user_id = users_collection.insert_one(user_dict).inserted_id
    return {"message": "User registered successfully", "user_id": str(user_id)}

@app.post("/login/")
async def login(username: str, password: str):
    existing_user = users_collection.find_one({"username": username})
    if existing_user and existing_user["password"] == password:
        return {"message": "Login successful", "user_id": str(existing_user["_id"])}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
@app.post("/address/")
async def add_address(address: Address):
    address_dict = address.dict()
    address_id = addresses_collection.insert_one(address_dict).inserted_id
    return {"message": "Address added successfully", "address_id": str(address_id)}

@app.post("/profile/")
async def add_profile(profile: Profile):
    profile_dict = profile.dict()
    profile_id = profiles_collection.insert_one(profile_dict).inserted_id
    return {"message": "Profile added successfully", "profile_id": str(profile_id)}