# Task Manager API

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)
![Pydantic](https://img.shields.io/badge/Pydantic-validation-E92063)
![Pytest](https://img.shields.io/badge/Pytest-tested-0A9EDC?logo=pytest)
![License](https://img.shields.io/github/license/xeclerx/task-manager)
![Last Commit](https://img.shields.io/github/last-commit/xeclerx/task-manager)

Backend REST API для управления задачами.

Проект реализован на **FastAPI**, **SQLAlchemy**, **Pydantic** и **PostgreSQL**.  
В проекте есть CRUD-операции для задач, валидация данных, работа с базой данных, тесты на `pytest` и логирование.

---

## Возможности

- Создание задач
- Получение списка задач
- Обновление задач
- Удаление задач
- Изменение статуса выполнения задачи
- Валидация входных и выходных данных через Pydantic
- Работа с PostgreSQL через SQLAlchemy ORM
- Разделение backend-приложения на слои
- Dependency Injection через FastAPI Depends
- Тестирование бизнес-логики через pytest
- Логирование работы приложения
- CORS для взаимодействия с frontend

---

## Стек технологий

- Python 3.12
- FastAPI
- PostgreSQL
- SQLAlchemy
- Pydantic
- Pytest
- Uvicorn
- Git

---

## Архитектура проекта

```text
Task_Manager_Project/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routers/
│   │   │   │   ├── __init__.py
│   │   │   │   └── task.py
│   │   │   ├── __init__.py
│   │   │   ├── dependencies.py
│   │   │   └── router.py
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   ├── config.py
│   │   │   └── logging.py
│   │   ├── db/
│   │   │   ├── __init__.py
│   │   │   └── session.py
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   └── task.py
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   └── task.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   └── task.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── task.py
│   │   ├── __init__.py
│   │   └── main.py
│   ├── tests/
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   └── test_task_service.py
│   │   ├── __init__.py
│   │   └── conftest.py
│   └── __init__.py
├── frontend/
└── requirements.txt
```

### Основные слои

- `api` — роутеры и зависимости FastAPI
- `routers` — HTTP-эндпоинты приложения
- `schemas` — Pydantic-схемы для валидации данных
- `models` — SQLAlchemy ORM-модели
- `repositories` — слой работы с базой данных
- `services` — бизнес-логика приложения
- `db` — подключение к базе данных
- `core` — конфигурация и логирование
- `tests` — тесты приложения на pytest

---

## API Endpoints

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks` | Получить список задач |
| POST | `/tasks` | Создать задачу |
| PATCH | `/tasks/{task_id}` | Обновить задачу |
| DELETE | `/tasks/{task_id}` | Удалить задачу |

---

## Примеры запросов

### Создание задачи

```json
{
  "title": "Изучить FastAPI"
}
```

### Обновление задачи

```json
{
  "title": "Изучить FastAPI и SQLAlchemy",
  "completed": true
}
```

---

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/xeclerx/task-manager.git
cd task-manager
```

### 2. Создать виртуальное окружение

```bash
python -m venv .venv
```

### 3. Активировать виртуальное окружение

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

### 4. Установить зависимости

```bash
pip install -r requirements.txt
```

### 5. Настроить PostgreSQL

Проверь строку подключения к базе данных в файле:

```text
backend/app/core/config.py
```

Пример строки подключения:

```text
postgresql+psycopg://postgres:admin@127.0.0.1:15432/postgres
```

### 6. Запустить приложение

Из корня проекта:

```bash
python -m uvicorn backend.app.main:app --reload
```

После запуска приложение будет доступно по адресу:

```text
http://127.0.0.1:8000
```

Swagger-документация:

```text
http://127.0.0.1:8000/docs
```

---

## Запуск тестов

```bash
pytest
```

---

## Логирование

В проекте используется логирование для отслеживания работы приложения и упрощения поиска ошибок во время разработки.

---

## Что реализовано

- REST API на FastAPI
- CRUD для задач
- PostgreSQL в качестве базы данных
- ORM-модели через SQLAlchemy
- Pydantic-схемы для проверки данных
- Dependency Injection через FastAPI Depends
- Разделение backend-приложения на слои
- Pytest-тесты для сервисного слоя
- Логирование
- Подключение CORS для frontend-приложения

---

## License

Проект распространяется под лицензией MIT. Подробнее см. файл [LICENSE](LICENSE).

---

## Автор

Олег Костенев  
Python Backend Developer
