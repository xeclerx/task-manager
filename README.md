# Task Manager API

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-009688?logo=fastapi)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-4169E1?logo=postgresql)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)
![Pydantic](https://img.shields.io/badge/Pydantic-validation-E92063)
![Pytest](https://img.shields.io/badge/Pytest-tested-0A9EDC?logo=pytest)
![License](https://img.shields.io/github/license/xeclerx/task-manager)
![Last Commit](https://img.shields.io/github/last-commit/xeclerx/task-manager)

Backend REST API для управления задачами и категориями.

Проект реализован на **FastAPI**, **SQLAlchemy**, **Pydantic** и **PostgreSQL**.  
В проекте есть CRUD-операции, валидация данных, работа с базой данных, тесты на `pytest` и логирование.

---

## Возможности

- Создание, получение, обновление и удаление задач
- Создание, получение, обновление и удаление категорий
- Валидация входных и выходных данных через Pydantic
- Работа с PostgreSQL через SQLAlchemy ORM
- Разделение проекта на слои: routers, services, repositories, models, schemas
- Dependency Injection через FastAPI Depends
- Тестирование через pytest
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
backend/
└── app/
    ├── api/
    │   ├── routers/
    │   ├── dependencies.py
    │   └── dependencies_category.py
    ├── core/
    │   └── config.py
    ├── db/
    │   └── session.py
    ├── models/
    │   ├── base.py
    │   ├── task.py
    │   └── category.py
    ├── repositories/
    │   ├── task.py
    │   └── category.py
    ├── schemas/
    │   ├── task.py
    │   └── category.py
    ├── services/
    │   ├── task.py
    │   └── category.py
    └── main.py
```

### Основные слои

- `routers` — обработка HTTP-запросов
- `schemas` — Pydantic-схемы для валидации данных
- `models` — SQLAlchemy ORM-модели
- `repositories` — слой работы с базой данных
- `services` — бизнес-логика приложения
- `db` — подключение к базе данных
- `core` — настройки проекта

---

## API Endpoints

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks` | Получить список задач |
| POST | `/tasks` | Создать задачу |
| PATCH | `/tasks/{task_id}` | Обновить задачу |
| DELETE | `/tasks/{task_id}` | Удалить задачу |

### Categories

| Method | Endpoint | Description |
|---|---|---|
| GET | `/categories` | Получить список категорий |
| POST | `/categories` | Создать категорию |
| PATCH | `/categories/{category_id}` | Обновить категорию |
| DELETE | `/categories/{category_id}` | Удалить категорию |

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

### Создание категории

```json
{
  "name": "Учёба"
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
- CRUD для задач и категорий
- PostgreSQL в качестве базы данных
- ORM-модели через SQLAlchemy
- Pydantic-схемы для проверки данных
- Dependency Injection через FastAPI Depends
- Разделение backend-приложения на слои
- Pytest-тесты
- Логирование
- Подключение CORS для frontend-приложения

---

## License

Проект распространяется под лицензией MIT. Подробнее см. файл [LICENSE](LICENSE).

---

## Автор

Олег Костенев  
Python Backend Developer
