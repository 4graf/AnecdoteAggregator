from fastapi import HTTPException
from starlette import status


# ToDo: добавить коды ошибок для внутреннего пользования


class RequestParamValidationError(HTTPException):
    def __init__(self, msg='Parameter validation failed.', exception_msg=''):
        super().__init__(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                         detail={"message": f"{msg}: {exception_msg}"})


class ResourceNotFoundByIDError(HTTPException):
    def __init__(self, msg='Resource not found by id.', exception_msg=''):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND,
                         detail={"message": f"{msg}: {exception_msg}"})


class AuthenticationUserError(HTTPException):
    def __init__(self, msg='Authentication error.', exception_msg=''):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail={"message": f"{msg}: {exception_msg}"})


