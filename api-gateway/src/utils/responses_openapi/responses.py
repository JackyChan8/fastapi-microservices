from fastapi import status

from src.utils.responses_openapi import schemas


def get_responses_openapi(description: str) -> dict:
    return {
        'description': description,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'detail': description
                    }
                }
            }
        }
    }


grpc_errors = {
    status.HTTP_500_INTERNAL_SERVER_ERROR: get_responses_openapi('Error connecting to the service by gRPC'),
}


auth_api = {
    'signup': {
        status.HTTP_201_CREATED: {'model': schemas.Response},
        status.HTTP_409_CONFLICT: get_responses_openapi('User already exists'),
        **grpc_errors,
    },
    'signin': {
        status.HTTP_200_OK: {'model': schemas.ResponseJWTToken},
        status.HTTP_409_CONFLICT: get_responses_openapi('Incorrect email or password'),
        **grpc_errors,
    }
}
