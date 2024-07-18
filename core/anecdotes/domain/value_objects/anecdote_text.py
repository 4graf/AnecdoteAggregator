from core.anecdotes.domain.exceptions import MinLengthAnecdoteError, MaxLengthAnecdoteError


class AnecdoteText:
    def __init__(self, text: str):
        if len(text) < 5:
            raise MinLengthAnecdoteError
        if len(text) > 3000:
            raise MaxLengthAnecdoteError

        self.text = text
