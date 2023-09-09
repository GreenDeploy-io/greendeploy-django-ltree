
import pytest

from django_ltree.fields import PathValue, PathValueProxy


def test_create():
    assert str(PathValue([1, 2, 3, 4, 5])) == '1.2.3.4.5'
    assert str(PathValue((1, 3, 5, 7))) == '1.3.5.7'
    assert str(PathValue('hello.world')) == 'hello.world'
    assert str(PathValue(5)) == "5"

    def generator():
        yield '100'
        yield 'bottles'
        yield 'of'
        yield 'beer'

    assert str(PathValue(generator())) == '100.bottles.of.beer'


def test_invalid_value_for_path():
    with pytest.raises(ValueError) as exc_info:
        PathValue(object())  # or any other invalid type that should raise the error
    assert "Invalid value" in str(exc_info.value)


def test_path_value_repr():
    pv = PathValue("1/2/3")
    assert repr(pv) == "1.2.3"

def test_path_value_str():
    pv = PathValue("1/2/3")
    assert str(pv) == "1.2.3"

def test_path_value_repr_with_dots():
    pv = PathValue("1.2.3")
    assert repr(pv) == "1.2.3"

def test_path_value_str_with_dots():
    pv = PathValue("1.2.3")
    assert str(pv) == "1.2.3"

# More tests for other types of input
def test_path_value_repr_with_list():
    pv = PathValue([1, 2, 3])
    assert repr(pv) == "1.2.3"

def test_path_value_str_with_list():
    pv = PathValue([1, 2, 3])
    assert str(pv) == "1.2.3"


class MockModel:
    def __init__(self):
        self.some_field = None


def test_path_value_proxy_get():
    proxy = PathValueProxy("some_field")
    mock_instance = MockModel()

    # Test the `if instance is None: return self` line
    assert proxy.__get__(None, MockModel) is proxy

    # Test the `if value is None: return value` line
    assert proxy.__get__(mock_instance, MockModel) is None


def test_path_value_proxy_set():
    proxy = PathValueProxy("some_field")
    mock_instance = MockModel()

    # Test the `if instance is None: return self` line
    try:
        proxy.__set__(None, "some_value")  # This won't raise an exception
    except Exception:
        pytest.fail("Should not raise any exceptions")

    # Set a value to test normal functionality
    proxy.__set__(mock_instance, "some_value")
    assert mock_instance.some_field == "some_value"