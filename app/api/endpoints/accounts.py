from fastapi import APIRouter
from app import schemas, models

router = APIRouter()


@router.get("/", response_model=list[schemas.Account])
async def list_accounts():
    return await models.Account.all().prefetch_related("owner")


