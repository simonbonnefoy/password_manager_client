import string

from pytest import fixture

from password_manager_client.helpers.strings import String


@fixture
def prepare_lower_ascii_string() -> str:
    return 'z'


@fixture()
def prepare_upper_ascii_string() -> str:
    return 'Z'


@fixture()
def prepare_digit_string() -> str:
    return '1'


def test_contains_string_method(prepare_lower_ascii_string,
                                prepare_upper_ascii_string,
                                prepare_digit_string
                                ):
    """
    Test String.contains_chars_from_list method
    @param prepare_lower_ascii_string: get ascii lower chars string
    @param prepare_upper_ascii_string: get ascii upper chars string
    @param prepare_digit_string: get digit string
    @return: None
    """
    lower_string = prepare_lower_ascii_string
    upper_string = prepare_upper_ascii_string
    digit_string = prepare_digit_string
    assert ((String.contains_chars_from_list(lower_string, string.ascii_lowercase)) and
            String.contains_chars_from_list(upper_string, string.ascii_uppercase) and not
            String.contains_chars_from_list(digit_string, string.ascii_uppercase))
