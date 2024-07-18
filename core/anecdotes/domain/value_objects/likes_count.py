from core.anecdotes.domain.exceptions import NegativeLikesCountError


class LikesCount:
    def __init__(self, count):
        if count < 0:
            raise NegativeLikesCountError

        self.count = count
