from motor.motor_asyncio import AsyncIOMotorClient

# async client for mongoDB
MONGODB_URL = "mongodb://mongo_db:27017/sbr_build"
client = AsyncIOMotorClient(MONGODB_URL)
database = client.sbr_build
builds_collection = database.builds
tasks_collection = database.tasks


def get_db():
    return database


def get_builds_collection():
    return builds_collection


def get_tasks_collection():
    return tasks_collection
