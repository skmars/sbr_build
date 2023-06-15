import re
from typing import List
from fastapi import HTTPException
from pydantic import BaseModel, Field, validator


# adjust class to make sure pydantic will convert even non-dict objects to json
class AdjustPydanticModel(BaseModel):
    class Config:
        orm_mode = True


# main Task schema in the case of self-referencing models).
class Task(BaseModel):
    name: str = Field(...)
    denendencies: List["Task"] = Field(...)


Task.update_forward_refs()

LETTER_MATCH_PATTERN = re.compile(r"^[a-z-A-Z\- _]+$")


# main Build schema
class Build(BaseModel):
    name: str = Field(...)
    tasks: List[Task] = Field(...)


# Request shema for tasks
class GetBuildTasks(BaseModel):
    build: str

    @validator("build")
    def validate_name(cls, value):
        if not LETTER_MATCH_PATTERN.match(value):
            raise HTTPException(
                status_code=422,
                detail="build name should contain string with only letters and underscores",
            )
        return value


# main Response schema
def ResponseModel(data):
    data: List[str]
    return data


def ErrorResponseModel(code, message):
    return {"code": code, "message": message}
