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

    @staticmethod
    def contains_from_list(string, special_characters):
        if any(c in special_characters for c in string):
            return True

        return False

    @staticmethod
    def generate_password(length=12,
                          contains_ascii_lowercase: bool = True,
                          contains_ascii_uppercase: bool = True,
                          contains_digits: bool = True,
                          contains_symbols: bool = True) -> str:
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
            password_is_valid = PasswordGenerator.contains_from_list(temp, symbols) & \
                                PasswordGenerator.contains_from_list(temp, num) & \
                                PasswordGenerator.contains_from_list(temp, lower) & \
                                PasswordGenerator.contains_from_list(temp, upper)

        password = "".join(temp)

        return password


if __name__ == '__main__':
    a = PasswordGenerator.generate_password(12, True, True, True, True,
                                            )
    print(a)
