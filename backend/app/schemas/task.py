from pydantic import BaseModel, ConfigDict


class TaskScheme(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    completed: bool


class TaskCreateScheme(BaseModel):
    title: str


class UpdateTaskScheme(BaseModel):
    title: str | None = None
    completed: bool | None = None
