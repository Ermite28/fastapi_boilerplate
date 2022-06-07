
from fastapi import FastAPI

from backend.apis.base import api_router
from backend.core.config import settings
from backend.db.base import Base
from backend.db.session import engine


def include_router(app):
    app.include_router(api_router)


def create_tables():
    print("Creating table")
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    include_router(app)
    create_tables()
    return app


app = start_application()