from app.core.anecdote.domain.exceptions import MaxLengthAnecdoteAuthorFirstNameError, \
    MaxLengthAnecdoteAuthorSecondNameError


def validate_name(name: str) -> bool:
    if len(name) > 60:
        return False
    return True


class AnecdoteAuthor:
    def __init__(self, first_name: str, second_name: str | None = None):
        if not validate_name(first_name):
            raise MaxLengthAnecdoteAuthorFirstNameError
        if second_name and not validate_name(second_name):
            raise MaxLengthAnecdoteAuthorSecondNameError

        self.first_name = first_name
        self.second_name = second_name
