import grpc
from sqlalchemy import select, exists
from google.protobuf.json_format import MessageToDict

from models import User
from protobuf import auth_pb2_grpc, auth_pb2
from database import async_session
from utils.auth import get_password_hash


class AuthService(auth_pb2_grpc.RequestCreateUserServicer):
    async def CreateUser(
            self,
            request: auth_pb2.ResponseCreateUser,
            context: grpc.aio.ServicerContext
    ) -> auth_pb2.ResponseCreateUser:
        data = MessageToDict(request)
        email, password = data.values()
        async with async_session() as session:
            query = select(exists(select(User.email).where(User.email == email)))
            exists_user = await session.scalar(query)
            if exists_user:
                context.set_code(grpc.StatusCode.ALREADY_EXISTS)
                context.set_details('User already exists')
                return auth_pb2.ResponseCreateUser()
            db_user = User(email=email, password=get_password_hash(password))
            session.add(db_user)
            await session.commit()
            await session.refresh(db_user)
            return auth_pb2.ResponseCreateUser(status=200, message='User successfully created')

    # async def Login(self,
    #                 request,
    #                 context):
