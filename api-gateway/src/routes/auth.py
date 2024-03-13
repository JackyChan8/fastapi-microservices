from fastapi import APIRouter, status

from src.schemas import auth as auth_schemas
from src.services import auth as auth_services


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/signup', status_code=status.HTTP_201_CREATED)
async def signup(user: auth_schemas.UserCreate):
    return await auth_services.create_user(user)


@router.post('/signin')
async def signin():
    pass
