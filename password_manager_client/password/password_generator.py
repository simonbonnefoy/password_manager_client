import random
import string
from password_manager_client.helpers.strings import String


class PasswordGenerator:
    """
    Class to create a new password
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    def __init__(self):
        ...


    def is_password_valid(self, password: str, contains_ascii_lowercase: bool, contains_ascii_uppercase: bool, contains_digits: bool,
                          contains_symbols: bool):
        """
        Check if the password is valid according to the characters it should contain
        @param password:  password to check
        @param contains_ascii_lowercase: Should the password contain lowercase
        @param contains_ascii_uppercase: Should the password contain uppercase
        @param contains_digits: Should the password contain digits
        @param contains_symbols: Should the password contain symbols
        @return: True if valid password False else
        """

        password_is_valid = ((String.contains_chars_from_list(password, self.lower) is contains_ascii_lowercase) &
                             (String.contains_chars_from_list(password, self.upper) is contains_ascii_uppercase) &
                             (String.contains_chars_from_list(password, self.digits) is contains_digits) &
                             (String.contains_chars_from_list(password, self.symbols) == contains_symbols))

        return password_is_valid

    def generate_password(self, length=12,
                          contains_ascii_lowercase: bool = True,
                          contains_ascii_uppercase: bool = True,
                          contains_digits: bool = True,
                          contains_symbols: bool = True) -> str:

        password_base_string = self.create_password_base_chars(contains_ascii_lowercase,
                                                          contains_ascii_uppercase,
                                                          contains_digits,
                                                          contains_symbols)
        password_is_valid = False
        while not password_is_valid:
            password = ''.join([random.choice(password_base_string) for _ in range(length)])
            password_is_valid = self.is_password_valid(password, contains_ascii_lowercase,
                                                                    contains_ascii_uppercase,
                                                                    contains_digits,
                                                                    contains_symbols)

        valid_password = "".join(password)

        return valid_password

    def create_password_base_chars(self,contains_ascii_lowercase: bool = True,
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

        password_base_string = []
        if contains_ascii_lowercase:
            password_base_string += self.lower

        if contains_ascii_uppercase:
            password_base_string += self.upper

        if contains_digits:
            password_base_string += self.digits

        if contains_symbols:
            password_base_string += self.symbols
        return password_base_string

if __name__ == '__main__':
    a = PasswordGenerator()
    b = a.generate_password(24, True, True, True, True)
    print(b)
