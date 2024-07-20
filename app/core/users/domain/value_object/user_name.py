from app.core.users.domain.exceptions import MinLengthUserFirstNameError, MinLengthUserSecondNameError, \
    MaxLengthUserSecondNameError, MaxLengthUserFirstNameError, UserError


def validate_name(name: str, less_exception: type[UserError], greater_exception: type[UserError]) -> None:
    if len(name) < 2:
        raise less_exception
    if len(name) > 60:
        raise greater_exception


class UserName:
    def __init__(self, first_name: str, second_name: str | None = None):
        validate_name(first_name, MinLengthUserFirstNameError, MaxLengthUserFirstNameError)
        validate_name(second_name, MinLengthUserSecondNameError, MaxLengthUserSecondNameError)

        self.first_name = first_name
        self.second_name = second_name
