from fastapi import APIRouter
from app.models.products import Product
from app.database.connection import products_collection
from app.schema.schemas import list_product
from bson import ObjectId

product = APIRouter()

# GET Request Methods
@product.get("/")
async def get_products():
    products = list_product(products_collection.find())
    return products

# POST Request Methods
@product.post("/")
async def post_product(product: Product):
    products_collection.insert_one(dict(product))
    return {"message": "Product added successfully"}

# PUT Request Methods
@product.put("/{id}")
async def put_product(id: str, product: Product):
    products_collection.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(product)})
    return {"message": "Product updated successfully"}

# DELETE Request Methods
@product.delete("/{id}")
async def delete_product(id: str):
    products_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "Product deleted successfully"}
