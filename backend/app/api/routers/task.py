from fastapi import APIRouter, status, Depends, HTTPException
from backend.app.schemas.task import TaskScheme, TaskCreateScheme, UpdateTaskScheme
from backend.app.services.task import TaskService, TaskNotFoundError
from backend.app.api.dependencies import get_task_service


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.get("", response_model=list[TaskScheme])
def get_tasks(service: TaskService = Depends(get_task_service)) -> list[TaskScheme]:
    return service.list_tasks()


@router.post("", response_model=TaskScheme, status_code=status.HTTP_201_CREATED)
def create_task(
        payload: TaskCreateScheme,
        task_service: TaskService = Depends(get_task_service)
) -> TaskScheme:
    return task_service.create_task(payload)


@router.patch("/{task_id}", response_model=TaskScheme)
def update_task(
        task_id: str,
        payload: UpdateTaskScheme,
        task_service: TaskService = Depends(get_task_service)
) -> TaskScheme:
    try:
        return task_service.update_task(task_id, payload)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Задача не найдена",
        )


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
        task_id: str,
        task_service: TaskService = Depends(get_task_service)
) -> None:
    try:
        task_service.delete_task(task_id)
    except TaskNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Задача не найдена",
        )
