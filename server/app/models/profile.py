# models/profile.py

from pydantic import BaseModel


class Profile(BaseModel):
    user_id: str
    card_id: str
    passport: str
    phone_number: str
    # Add other necessary fields
