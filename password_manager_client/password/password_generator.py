import random
import string


class PasswordGenerator:
    def __init__(self, length=12,
                 contains_ascii_lowercase=True,
                 contains_ascii_uppercase=True,
                 contains_digits=True,
                 contains_symbols=True):
        self.length = length
        self.contains_ascii_lowercase = contains_ascii_lowercase
        self.contains_ascii_uppercase = contains_ascii_uppercase
        self.contains_ascii_digits = contains_digits
        self.contains_ascii_symbols = contains_symbols

    def generate_password(self) -> str:
        length = random.randint(12, 25)
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        all = lower + upper + num + symbols

        temp = random.sample(all, length)

        password = "".join(temp)

        print(password)
        return password
