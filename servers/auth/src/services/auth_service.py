import grpc
from sqlalchemy import select, exists
from google.protobuf.json_format import MessageToDict

from models import User
from database import async_session
from protobuf import auth_pb2_grpc, auth_pb2
from utils.auth import get_password_hash, verify_password, create_access_token


class AuthService(auth_pb2_grpc.RequestAuthUserServicer):
    async def CreateUser(
            self,
            request: auth_pb2.RequestDataUser,
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
            return auth_pb2.ResponseCreateUser(status=201, message='User successfully created')

    async def LoginUser(self,
                        request: auth_pb2.RequestDataUser,
                        context: grpc.aio.ServicerContext) -> auth_pb2.ResponseLogin:
        data = MessageToDict(request)
        email, password = data.values()
        async with async_session() as session:
            query = select(exists(select(User.email).where(User.email == email)))
            exists_user = await session.scalar(query)
            if not exists_user:
                context.set_code(grpc.StatusCode.UNAUTHENTICATED)
                context.set_details('Incorrect email or password')
                return auth_pb2.ResponseLogin()
            db_user = await session.execute(select(User.user_id, User.password).where(User.email == email))
            db_user = db_user.one()
            if not verify_password(password, db_user.password):
                context.set_code(grpc.StatusCode.UNAUTHENTICATED)
                context.set_details('Incorrect email or password')
                return auth_pb2.ResponseLogin()

            access_token = create_access_token(data={"sub": str(db_user.user_id)})
            return auth_pb2.ResponseLogin(access_token=access_token)

