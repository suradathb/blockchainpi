# app/routers/profile.py
from fastapi import APIRouter, HTTPException
from app.models.profile import Profile
from app.database import get_db

router = APIRouter()

@router.get("/profiles/{profile_id}", response_model=Profile)
async def get_profile(profile_id: str):
    db = get_db()
    profile = db.get_profile_by_id(profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.post("/profiles/", response_model=Profile)
async def create_profile(profile: Profile):
    db = get_db()
    created_profile = db.create_profile(profile)
    return created_profile
