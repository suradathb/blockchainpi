from bson import ObjectId

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
        "user_id": address["user_id"],
        "street": address["street"],
        "city": address["city"],
        "state": address["state"],
        "postal_code": address["postal_code"],
        "country": address["country"]
    }

def list_address(addresses) -> list:
    return[user_serial(address) for address in addresses]

def profile_serial(profile) -> dict:
    return {
        "id": str(profile["_id"]),
        "user_id": profile["user_id"],
        "card_id": profile["current_address"],
        "passport": profile["passport"],
        "phone_number": profile["phone_number"]
    }

def list_profile(profiles) -> list:
    return[user_serial(profiles) for profiles in profiles]