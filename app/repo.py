# repositories/user_repo.py
from config import db

async def get_all_users():
    return await db.database["users"].find().to_list(100)

async def create_user(data: dict):
    return await db.database["users"].insert_one(data)
