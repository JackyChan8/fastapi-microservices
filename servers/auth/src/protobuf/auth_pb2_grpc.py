# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protobuf import auth_pb2_grpc, auth_pb2


class RequestCreateUserStub(object):
    """Request 'Create User'
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateUser = channel.unary_unary(
                '/auth.RequestCreateUser/CreateUser',
                request_serializer=auth_pb2.RequestDataUser.SerializeToString,
                response_deserializer=auth_pb2.ResponseCreateUser.FromString,
                )


class RequestCreateUserServicer(object):
    """Request 'Create User'
    """

    def CreateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RequestCreateUserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateUser,
                    request_deserializer=auth_pb2.RequestDataUser.FromString,
                    response_serializer=auth_pb2.ResponseCreateUser.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.RequestCreateUser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RequestCreateUser(object):
    """Request 'Create User'
    """

    @staticmethod
    def CreateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.RequestCreateUser/CreateUser',
            auth_pb2.RequestDataUser.SerializeToString,
            auth_pb2.ResponseCreateUser.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class RequestLoginUserStub(object):
    """Request 'Login'
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.LoginUser = channel.unary_unary(
                '/auth.RequestLoginUser/LoginUser',
                request_serializer=auth_pb2.RequestDataUser.SerializeToString,
                response_deserializer=auth_pb2.ResponseLogin.FromString,
                )


class RequestLoginUserServicer(object):
    """Request 'Login'
    """

    def LoginUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RequestLoginUserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'LoginUser': grpc.unary_unary_rpc_method_handler(
                    servicer.LoginUser,
                    request_deserializer=auth_pb2.RequestDataUser.FromString,
                    response_serializer=auth_pb2.ResponseLogin.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'auth.RequestLoginUser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class RequestLoginUser(object):
    """Request 'Login'
    """

    @staticmethod
    def LoginUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/auth.RequestLoginUser/LoginUser',
            auth_pb2.RequestDataUser.SerializeToString,
            auth_pb2.ResponseLogin.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)