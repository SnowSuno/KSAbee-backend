from fastapi import APIRouter
from .endpoints import accounts

router = APIRouter()

router.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
