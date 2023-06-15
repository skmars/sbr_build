import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from app.api.routes.tasks import tasks_router
from app.manage_files.preload import lifespan


description = """
The Saber Build System for GameDev for allowing machines to create builds automatically.. 🤖

## Tasks
By **build name** you will be able to
get tasks sorted due to its dependencies.
"""
app = FastAPI(
    title="SaberBuild", description=description, version="0.1", lifespan=lifespan
)

# instance for routers
main_api_router = APIRouter()


# set a single router to the app instance
main_api_router.include_router(tasks_router, tags=["tasks"])
app.include_router(main_api_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
