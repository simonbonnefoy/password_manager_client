import random
import string


def create_password_base_chars(contains_ascii_lowercase: bool = True,
                               contains_ascii_uppercase: bool = True,
                               contains_digits: bool = True,
                               contains_symbols: bool = True) -> list:
    """
    Create a list containing all the chars to be used to create a password
    @param contains_ascii_lowercase: Use ascii lowercase
    @param contains_ascii_uppercase: Use ascii uppercase
    @param contains_digits: use digits
    @param contains_symbols: use symbols
    @return: list containing all the chars to be used to create a password
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    password_base_string = []
    if contains_ascii_lowercase:
        password_base_string += lower

    if contains_ascii_uppercase:
        password_base_string += upper

    if contains_digits:
        password_base_string += num

    if contains_symbols:
        password_base_string += symbols
    return password_base_string


class PasswordGenerator:
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    def __init__(self):
        ...

    @staticmethod
    def contains_from_list(string, char_list):
        """
        Check if a string contains any of the characters from a list
        for example: string = 'ac' and char_list = ['a','b'] returns True
        string = 'ac' and char_list = ['d','e'] returns True
        @param string: string to check
        @param char_list: list containing the characters to check, whether present in the list or not
        @return:  bool
        """
        if any(c in char_list for c in string):
            return True

        return False

    @staticmethod
    def generate_password(length=12,
                          contains_ascii_lowercase: bool = True,
                          contains_ascii_uppercase: bool = True,
                          contains_digits: bool = True,
                          contains_symbols: bool = True) -> str:

        password_base_string = create_password_base_chars(contains_ascii_lowercase,
                                                          contains_ascii_uppercase,
                                                          contains_digits,
                                                          contains_symbols)
        password_is_valid = False
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits*2
        symbols = string.punctuation
        while not password_is_valid:
            print('hello')
            temp = ''.join([random.choice(password_base_string) for _ in range(length)])
            # temp = random.sample(password_base_string, length)
            password_is_valid = ((PasswordGenerator.contains_from_list(temp, lower) is contains_ascii_lowercase) &
                                 (PasswordGenerator.contains_from_list(temp, upper) is contains_ascii_uppercase) &
                                 (PasswordGenerator.contains_from_list(temp, digits) is contains_digits) &
                                 (PasswordGenerator.contains_from_list(temp, symbols) == contains_symbols))

        password = "".join(temp)

        return password


if __name__ == '__main__':
    # a = PasswordGenerator.generate_password(12, True, True, True, True,
    #                                         )
    # print(a)
    a = PasswordGenerator.generate_password(12, True, True, True,True,
                                            )
    print(a)
