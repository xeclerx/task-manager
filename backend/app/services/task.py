from sqlalchemy.orm import Session
from backend.app.repositories.task import TaskRepository
from backend.app.schemas.task import TaskScheme, TaskCreateScheme, UpdateTaskScheme


class TaskNotFoundError(Exception):
    pass


class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db)

    def list_tasks(self) -> list[TaskScheme]:
        tasks_orm = self.task_repository.get_all()
        return [TaskScheme.model_validate(task) for task in tasks_orm]

    def create_task(self, payload: TaskCreateScheme) -> TaskScheme:
        task_orm = self.task_repository.create(title=payload.title)
        self.db.commit()
        return TaskScheme.model_validate(task_orm)

    def update_task(self, task_id: str, payload: UpdateTaskScheme) -> TaskScheme:
        task_for_update = self.task_repository.get_by_id(task_id=task_id)
        if not task_for_update:
            raise TaskNotFoundError(f'Задача с {task_id} не найдена!')

        if task_for_update.title:
            task_for_update.title = payload.title
        if task_for_update.completed is not None:
            task_for_update.completed = payload.completed

        self.db.commit()
        return TaskScheme.model_validate(task_for_update)

    def delete_task(self, task_id: str):
        task_for_delete = self.task_repository.get_by_id(task_id=task_id)
        if task_for_delete is None:
            raise TaskNotFoundError(f'Задача с {task_id} не найдена!')

        self.task_repository.delete(task_for_delete)
        self.db.commit()
