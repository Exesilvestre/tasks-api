from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool
from dotenv import load_dotenv
import os
from typing import Generator

import settings


load_dotenv()

engine = create_engine(settings.settings.DATABASE_URL)


class SessionManager:
    _engine = None
    _SessionLocal = None

    @classmethod
    def initialize(cls):
        if cls._engine is None:
            cls._engine = create_engine(settings.settings.DATABASE_URL, poolclass=NullPool, echo=False)
            cls._SessionLocal = sessionmaker(bind=cls._engine)

    @classmethod
    def get_session(cls) -> Session:
        if cls._SessionLocal is None:
            cls.initialize()
        return cls._SessionLocal()


def get_session() -> Generator[Session, None, None]:
    session = SessionManager.get_session()
    try:
        yield session
    finally:
        session.close()