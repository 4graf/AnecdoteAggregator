import re

from app.core.user.domain.exceptions import IncorrectEmailError


# Простая проверка на '@' и '.' в почтовом адресе.
# ToDo: использовать функцию с проверкой по SMTP (в любом случае понадобится отправлять письмо для подтверждения
#  почты, поэтому можно и не делать сложных проверок)
def validate_email(email: str) -> bool:
    email_regex = r'[^@]+@[^@]+\.[^@]+'
    if re.fullmatch(email_regex, email):
        return True
    return False


class Email:
    def __init__(self, email: str):
        if not validate_email(email):
            raise IncorrectEmailError
        self.email = email
