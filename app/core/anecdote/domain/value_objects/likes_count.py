from app.core.anecdote.domain.exceptions import NegativeLikesCountError


class LikesCount:
    def __init__(self, count: int):
        if count < 0:
            raise NegativeLikesCountError

        self.count = count
