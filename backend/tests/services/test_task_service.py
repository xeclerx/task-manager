from unittest.mock import Mock

import pytest

from backend.app.models.task import TaskORM
from backend.app.schemas.task import TaskScheme, TaskCreateScheme, UpdateTaskScheme
from backend.app.services.task import TaskNotFoundError, TaskService


def test_list_tasks_returns_pydantic_models(
    service: TaskService,
    repository_mock: Mock,
) -> None:
    # Имитируем, что метод get_all репозитория вернет эти задачи
    repository_mock.get_all.return_value = [
        TaskORM(id="task-1", title="Изучить pytest", completed=False),
        TaskORM(id="task-2", title="Написать первый тест", completed=True),
    ]

    result = service.list_tasks()

    assert result == [
        TaskScheme(id="task-1", title="Изучить pytest", completed=False),
        TaskScheme(id="task-2", title="Написать первый тест", completed=True),
    ]


def test_create_task_commits_created_task(
    service: TaskService,
    db_mock: Mock,
    repository_mock: Mock,
) -> None:
    created_task = TaskORM(id="task-1", title="Новая задача", completed=False)
    repository_mock.create.return_value = created_task

    result = service.create_task(TaskCreateScheme(title="Новая задача"))

    repository_mock.create.assert_called_once_with(title="Новая задача")
    db_mock.commit.assert_called_once_with()
    assert result.model_dump() == {
        "id": "task-1",
        "title": "Новая задача",
        "completed": False,
    }


@pytest.mark.parametrize(
    ("payload", "expected_title", "expected_completed"),
    [
        pytest.param(
            UpdateTaskScheme(title="Обновить заголовок"),
            "Обновить заголовок",
            False,
            id="updates-title",
        ),
        pytest.param(
            UpdateTaskScheme(completed=True),
            "Старая задача",
            True,
            id="updates-completed-flag",
        ),
        pytest.param(
            UpdateTaskScheme(title="Готово", completed=True),
            "Готово",
            True,
            id="updates-both-fields",
        ),
    ],
)
def test_update_task_updates_only_passed_fields(
    service: TaskService,
    db_mock: Mock,
    repository_mock: Mock,
    payload: UpdateTaskScheme,
    expected_title: str,
    expected_completed: bool,
) -> None:
    task = TaskORM(id="task-1", title="Старая задача", completed=False)
    repository_mock.get_by_id.return_value = task

    result = service.update_task("task-1", payload)

    repository_mock.get_by_id.assert_called_once_with("task-1")
    db_mock.commit.assert_called_once_with()
    assert result.model_dump() == {
        "id": "task-1",
        "title": expected_title,
        "completed": expected_completed,
    }


def test_update_task_raises_when_task_not_found(
    service: TaskService,
    db_mock: Mock,
    repository_mock: Mock,
) -> None:
    repository_mock.get_by_id.return_value = None

    with pytest.raises(TaskNotFoundError):
        service.update_task("missing-task", UpdateTaskScheme(title="Неважно"))

    db_mock.commit.assert_not_called()


def test_delete_task_removes_task_and_commits(
    service: TaskService,
    db_mock: Mock,
    repository_mock: Mock,
) -> None:
    task = TaskORM(id="task-1", title="Удалить задачу", completed=False)
    repository_mock.get_by_id.return_value = task

    service.delete_task("task-1")

    repository_mock.delete.assert_called_once_with(task)
    db_mock.commit.assert_called_once_with()


def test_delete_task_raises_when_task_not_found(
    service: TaskService,
    db_mock: Mock,
    repository_mock: Mock,
) -> None:
    # Имитируем, что задача не найдена в БД (None)
    repository_mock.get_by_id.return_value = None

    with pytest.raises(TaskNotFoundError):
        service.delete_task("missing-task")

    repository_mock.delete.assert_not_called()
    db_mock.commit.assert_not_called()
