from fastapi import APIRouter
from app.api.handlers.tasks import get_build_tasks, get_sorted_tasks
from app.api.schemas import GetBuildTasks, ResponseModel, ErrorResponseModel


tasks_router = APIRouter()


# Endpoints for tasks
@tasks_router.post("/get_tasks")
async def get_tasks(build: GetBuildTasks):
    if not await get_build_tasks(build):
        return ErrorResponseModel(404, "Tasks not found")
    sorted_tasks = await get_sorted_tasks(build)
    if not sorted_tasks:
        return ErrorResponseModel(404, "There is an error while getting sorted tasks")
    return ResponseModel(sorted_tasks)
