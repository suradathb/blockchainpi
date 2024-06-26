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
from app.routers.addresses import router_address as address_router
from app.routers.profiles import profile_router as profile_router
from bson import ObjectId


app = FastAPI()

app.include_router(todo_router, prefix="/todos", tags=["Todos"])
app.include_router(product_router, prefix="/products", tags=["Products"])
app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(address_router, prefix="/address", tags=["Address"])
app.include_router(profile_router, prefix="/profiles", tags=["Profiles"])






