import asyncio
import grpc
from loguru import logger

from protobuf import auth_pb2_grpc, auth_pb2

from services.auth_service import AuthService

LISTENER_ADDR = '[::]:50000'


async def serve() -> None:
    server = grpc.aio.server()
    auth_pb2_grpc.add_RequestCreateUserServicer_to_server(AuthService(), server)
    server.add_insecure_port(LISTENER_ADDR)
    logger.info("Starting server on %s", LISTENER_ADDR)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    asyncio.run(serve())
