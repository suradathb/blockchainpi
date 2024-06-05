
from bson import ObjectId
from pymongo.collection import Collection

def individual_serial(todo) -> dict:
    return {
        "id":str(todo["_id"]),
        "name":todo["name"],
        "description":todo["description"],
        "complete":todo["complete"]
    }

def list_serial(todos) -> list:
    return[individual_serial(todo) for todo in todos]

def individual_product(product) -> dict:
    return {
        "id":str(product["_id"]),
        "name":product["name"],
        "description":product["description"],
        "price":product["price"],
        "stock":product["stock"],
        "minimum":product["minimum"],
        "status":product["status"]
    }

def list_product(products) -> list:
    return[individual_product(product) for product in products]

def user_serial(user) -> dict:
    return {
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "login_source": user["login_source"]
    }

def list_user(users) -> list:
    return[user_serial(user) for user in users]

def list_user_id(users, user_id=None) -> list:
    if user_id:
        user = users.find_one({"_id": ObjectId(user_id)})
        if user:
            return [user_serial(user)]
        else:
            return []
    else: 
        return [user_serial(user) for user in users]

def address_serial(address) -> dict:
    return {
        "id": str(address["_id"]),
        "user_id": str(address["user_id"]),
        "street": address["street"],
        "city": address["city"],
        "state": address["state"],
        "postal_code": address["postal_code"],
        "country": address["country"]
    }

def list_address(addresses) -> list:
    return[address_serial(address) for address in addresses]

def profile_serial(profile) -> dict:
    return {
        "id": str(profile["_id"]),
        "user_id": str(profile["user_id"]),
        "card_id": profile["card_id"],
        "passport": profile["passport"],
        "phone_number": profile["phone_number"]
    }

def list_profile(profiles) -> list:
    return[profile_serial(profile) for profile in profiles]

# def list_user_id(users_collection, addresses_collection, profiles_collection, user_id=None) -> dict:
#     try:
#         object_id = ObjectId(user_id)
#     except Exception as e:
#         print(f"Error converting user_id to ObjectId: {e}")
#         return None

#     user = users_collection.find_one({"_id": object_id})
#     if user:
#         user_data = user_serial(user)
#         address = addresses_collection.find_one({"user_id": object_id})
#         profile = profiles_collection.find_one({"user_id": object_id})
#         # Debugging statements to verify data
#         print(f"user_id: {object_id}")
#         print(f"Address found: {address}")
#         print(f"Profile found: {profile}")
#         if address:
#             user_data["address"] = address_serial(address)
#         else:
#             user_data["address"] = None
#         if profile:
#             user_data["profile"] = profile_serial(profile)
#         else:
#             user_data["profile"] = None
#         return user_data
#     else:
#         print(f"User not found with id: {user_id}")
#         return None
