import grpc
from fastapi import status, HTTPException
from google.protobuf.json_format import MessageToDict

from src.core.config import settings
from src.utils.grpc_status import grpc_status
from src.schemas.auth import UserCreate, UserLogin
from src.protobuf.auth import auth_pb2, auth_pb2_grpc


async def create_user(user: UserCreate):
    async with grpc.aio.insecure_channel(settings.AUTH_GRPC_ADDRESS) as channel:
        try:
            client = auth_pb2_grpc.RequestAuthUserStub(channel)
            request = auth_pb2.RequestDataUser(email=user.email, password=user.password)
            response = await client.CreateUser(request)
            return MessageToDict(response)
        except grpc.RpcError as e:
            status_code = grpc_status.get(e.code(), status.HTTP_500_INTERNAL_SERVER_ERROR)
            raise HTTPException(status_code=status_code, detail=e.details())


async def login_user(user: UserLogin):
    async with grpc.aio.insecure_channel(settings.AUTH_GRPC_ADDRESS) as channel:
        try:
            client = auth_pb2_grpc.RequestAuthUserStub(channel)
            request = auth_pb2.RequestDataUser(email=user.email, password=user.password)
            response = await client.LoginUser(request)
            return MessageToDict(response)
        except grpc.RpcError as e:
            status_code = grpc_status.get(e.code(), status.HTTP_500_INTERNAL_SERVER_ERROR)
            raise HTTPException(status_code=status_code, detail=e.details())

