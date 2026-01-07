# repositories/user_repo.py
from app.config import db
from bson import ObjectId

async def get_all_users():
    return await db.database["users"].find().to_list(100)

async def create_user(data: dict):
    return await db.database["users"].insert_one(data)

async def get_user_by_id(id:str):
    user =  await db.database["users"].find_one({"_id": ObjectId(id)})
    if not user:
        return None
    return user

async def update_user(id: str, data: dict):
        result = await db.database["users"].update_one(
            {"_id": ObjectId(id)},
            {"$set": data}
        )

        if result.matched_count == 0:
            return None

        user = await db.database["users"].find_one({"_id": ObjectId(id)})
        return user
async def delete_user(self,id:str):
    # user = await db.database["users"].find_one({"_id": ObjectId(id)})
    # if not user:
    #     return None
    # await db.database["users"].delete_one({"_id": ObjectId(id)})
    user = await db.database["users"].find_one_and_delete({"_id": ObjectId(id)})
    if not user:
        return None
    return user

async def search_user(input:str):
    user =  await db.database["users"].find().to_list(100)
    result = []
    search_term = input.lower()
    for data in user:
        if search_term in str(data).lower():
            result.append(data)
    return result
     

