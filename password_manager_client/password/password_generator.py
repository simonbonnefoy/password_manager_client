import random
import string


class PasswordGenerator:
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    def __init__(self):
        ...

    @staticmethod
    def check_if_contains_lowercase(string):
        lower = string.ascii_lowercase
        for character in string:
            if character in lower:
                return True

        return False
    @staticmethod
    def generate_password(length=12,
                          contains_ascii_lowercase: bool = True,
                          contains_ascii_uppercase: bool = True,
                          contains_digits: bool = True,
                          contains_symbols: bool = True) -> str:
        length = random.randint(12, 25)
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        all = []
        if contains_ascii_lowercase:
            all += lower

        if contains_ascii_uppercase:
            all += upper

        if contains_digits:
            all += num

        if contains_symbols:
            all += symbols

        password_is_valid = False
        while not password_is_valid:
            temp = random.sample(all, length)
            # Make a way to check if password contains all requireds chars
            password_is_valid = True

        password = "".join(temp)

        return password

if __name__ == '__main__':
    a = PasswordGenerator.generate_password(12, True, True, True, True,
                                        )