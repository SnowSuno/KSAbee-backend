from fastapi import FastAPI

from app.core.config import settings
from app.core.database import db_init
from app import api

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(api.router)

db_init(app)
