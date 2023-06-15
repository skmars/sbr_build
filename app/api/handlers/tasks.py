from typing import List
from fastapi.encoders import jsonable_encoder
from app.db.crud import get_doc
from app.db.settings import get_builds_collection, get_tasks_collection


async def get_build_tasks(build):
    builds_collection = get_builds_collection()
    encoded_build = jsonable_encoder(build)
    build_tasks = await get_doc(
        val=encoded_build["build"], collection=builds_collection
    )
    if build_tasks:
        return build_tasks["tasks"]
    return None


async def get_dependencies(task_name: str):
    tasks_collection = get_tasks_collection()
    task_data = await get_doc(val=task_name, collection=tasks_collection)
    return task_data["dependencies"]


async def _flatten(tasks: List[str]):
    for t in tasks:
        dependencies = await get_dependencies(t)
        if isinstance(dependencies, list):
            if len(dependencies) > 0:
                async for d in _flatten(dependencies):
                    yield d
            yield t


async def _flatten_tasks(tasks: List[str]) -> List[str]:
    flatten_tasks = [t async for t in _flatten(tasks)]
    res = [*flatten_tasks]
    return res


async def get_sorted_tasks(build):
    tasks = await get_build_tasks(build)
    if tasks:
        sorted_tasks = await _flatten_tasks(tasks)
        return sorted_tasks
    return None
