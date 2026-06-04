import logging
from time import perf_counter
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from backend.app.models.base import Base
from backend.app.db.session import engine

from starlette.middleware.base import RequestResponseEndpoint

from backend.app.core.config import get_settings
from backend.app.core.logging import configure_logging
from backend.app.api.router import api_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


configure_logging()

settings = get_settings()
app = FastAPI(lifespan=lifespan)
logger = logging.getLogger("app.middleware")  # Название логгера в логах

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_allowed_origin,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

cnt = 0


# Выполняется до и после обработки каждого HTTP-запроса.
@app.middleware("http")
async def log_requests(
    request: Request,
    call_next: RequestResponseEndpoint,
) -> Response:
    started_at = perf_counter()
    try:
        response: Response = await call_next(request)  # Работа самого эндпоинта
    except Exception:
        duration_ms = (perf_counter() - started_at) * 1000
        logger.exception(
            "Request failed: %s %s completed_in=%.2fms",
            request.method,
            request.url.path,
            duration_ms,
        )
        raise

    duration_ms = (perf_counter() - started_at) * 1000
    logger.info(
        "%s %s -> %s (%.2f ms)",
        request.method,
        request.url.path,
        response.status_code,
        duration_ms,
    )
    return response


@app.middleware("http")
async def http_counter(
    request: Request,
    call_next: RequestResponseEndpoint,
) -> Response:
    global cnt
    cnt += 1
    response: Response = await call_next(request)
    response.headers["X-Request-Number"] = str(cnt)
    return response

app.include_router(api_router)
