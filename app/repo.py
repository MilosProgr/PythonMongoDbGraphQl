# repositories/user_repo.py
from config import db
from bson import ObjectId

async def get_all_users():
    countDocuments = await db.database["users"].count_documents({})
    print(f"Broj dokumenata:   {countDocuments}" )
    return await db.database["users"].find().to_list(100)

async def get_user_by_id(self,id:str):
    user =  await db.database["users"].find_one({"_id": ObjectId(id)})
    if not user:
        return None
    return user

async def create_user(data: dict):
    return await db.database["users"].insert_one(data)

async def update_user(self, id: str, data: dict):
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
