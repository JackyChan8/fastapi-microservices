from fastapi import APIRouter, status

from src.schemas import auth as auth_schemas
from src.services import auth as auth_services

from src.utils.responses_openapi.responses import auth_api


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/signup',
             status_code=status.HTTP_201_CREATED,
             responses={**auth_api.get('signup')})
async def signup(user: auth_schemas.UserCreate):
    return await auth_services.create_user(user)


@router.post('/signin',
             status_code=status.HTTP_200_OK,
             responses={**auth_api.get('signin')})
async def signin(user: auth_schemas.UserLogin):
    return await auth_services.login_user(user)
