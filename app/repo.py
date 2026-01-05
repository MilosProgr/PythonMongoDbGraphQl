# repositories/user_repo.py
from app.config import db
from bson import ObjectId

async def get_all_users():
    countDocuments = await db.database["users"].count_documents({})
    name = db.database["users"]
    async for index in await name.list_indexes():
        print("Indeksi: ", index)

    print(f"Broj dokumenata:   {countDocuments} ime {name.distinct("name")}" )
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
