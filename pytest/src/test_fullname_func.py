
from fullname_func import get_full_name


def test_get_full_name_without_middle_name():
    assert get_full_name("John", "Doe") == "John Doe"
    assert get_full_name("Jane", "Smith") == "Jane Smith"

def test_get_full_name_with_middle_name():
    assert get_full_name("John", "Doe", "Michael") == "John Michael Doe"

test_get_full_name_without_middle_name()
test_get_full_name_with_middle_name()

