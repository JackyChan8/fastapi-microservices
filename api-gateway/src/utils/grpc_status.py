import grpc
from fastapi import status

grpc_status = {
    grpc.StatusCode.ALREADY_EXISTS: status.HTTP_409_CONFLICT,
}
