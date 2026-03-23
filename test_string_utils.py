import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive_test
@pytest.mark.parametrize(
    "input_str, expected",[
    ("phone", "Phone"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ]
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize(
    "input_str , expected",[
        ("  File", "File"),
        (" _Cat", "_Cat"),
        (" test123","test123"),
    ]
)
def test_trim_positive(input_str,expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.parametrize(
    "input_str, input_symbol, expected",[
        ("123457","3", True),
        ("tEST%@$&","@", True),
        ("Hello world !", "!", True),
    ]
)
def test_contains_positive(input_str,input_symbol,expected):
    assert string_utils.contains(input_str,input_symbol) == expected

@pytest.mark.parametrize(
    "input_str, input_symbol, expected",[
        ("Testb123","b","Test123"),
        ("Hello world","H","ello world"),
        ("Pyt@hon","@","Python"),
    ]
)
def test_delete_symbol_positive(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected

@pytest.mark.negative_test
@pytest.mark.parametrize(
    "input_str, expected",[
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ]
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.parametrize(
    "input_str , expected",[
        (" File", "ile"),
        (" _Cat", "Cat"),
        ("   test123","test"),
    ]
)
def test_trim_negative(input_str,expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.parametrize(
    "input_str, input_symbol, expected",[
        ("123457","9", True),
        ("tEST%@$&","*", True),
        ("Hello world !", "5", True),
    ]
)
def test_contains_negative(input_str,input_symbol,expected):
    assert string_utils.contains(input_str,input_symbol) == expected

@pytest.mark.parametrize(
    "input_str, input_symbol, expected",[
        ("Testb123","e","Test123"),
        ("Hello world","Hello","world"),
        ("Pyt@hon","@"," "),
    ]
)
def test_delete_symbol_negative(input_str, input_symbol, expected):
    assert string_utils.delete_symbol(input_str, input_symbol) == expected