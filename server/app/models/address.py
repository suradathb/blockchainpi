# models/address.py

from pydantic import BaseModel

class Address(BaseModel):
    user_id: str
    street: str
    city: str
    state: str
    postal_code: str
    country : str
