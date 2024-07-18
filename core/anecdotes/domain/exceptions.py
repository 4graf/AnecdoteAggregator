class AnecdoteError(Exception):
    """Базовое исключение для пользователей"""


class MaxLengthAnecdoteAuthorFirstNameError(AnecdoteError):

    def __init__(self, msg='Anecdote author has a first name greater than the maximum.'):
        super().__init__(msg)


class MaxLengthAnecdoteAuthorSecondNameError(AnecdoteError):

    def __init__(self, msg='Anecdote author has a second name greater than the maximum.'):
        super().__init__(msg)


class MinLengthAnecdoteError(AnecdoteError):

    def __init__(self, msg='Anecdote has a length less than the minimum.'):
        super().__init__(msg)


class MaxLengthAnecdoteError(AnecdoteError):

    def __init__(self, msg='Anecdote has a length grater than the maximum.'):
        super().__init__(msg)


class NegativeLikesCountError(AnecdoteError):

    def __init__(self, msg='Likes count cannot be negative.'):
        super().__init__(msg)


class AnecdoteNotFoundError(AnecdoteError):
    """Исключение, возникающее при не нахождении анекдота"""

    def __init__(self, msg='Anecdote not found.'):
        super().__init__(msg)
