from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi import HTTPException
from .decode_yaml import get_yaml_data
from app.db.crud import create_collection, delete_collection
from app.db.settings import get_builds_collection, get_tasks_collection


# preload yaml files to DB before on startup and remove after shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    tasks_collection = get_tasks_collection()
    tasks = get_yaml_data("./builds/tasks.yaml.docx")
    for t in tasks["tasks"]:
        tasks_coll = await create_collection(doc_data=t, collection=tasks_collection)
        if not tasks_coll:
            raise HTTPException(status_code=503, detail="Database error")

    builds = get_yaml_data("./builds/builds.yaml.docx")
    builds_collection = get_builds_collection()
    for b in builds["builds"]:
        build_coll = await create_collection(doc_data=b, collection=builds_collection)
        if not build_coll:
            raise HTTPException(status_code=503, detail="Database error")
    yield
    await delete_collection(tasks_collection)
    await delete_collection(builds_collection)
