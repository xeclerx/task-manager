from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from backend.app.core.config import get_settings
from collections.abc import Generator


settings = get_settings()
engine = create_engine(settings.DATABASE_URL)
Sessionlocal = sessionmaker(bind=engine)


def get_db() -> Generator[Session, None, None]:
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()
