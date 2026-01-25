import pytest
from string_utils import StringUtils

# Тесты для capitilize
def test_capitilize_positive():
    string_utils = StringUtils()
    res = string_utils.capitilize("skypro")
    assert res == "Skypro"

def test_capitilize_empty_string():
    string_utils = StringUtils()
    res = string_utils.capitilize("")
    assert res == ""

def test_capitilize_with_whitespace():
    string_utils = StringUtils()
    res = string_utils.capitilize(" ")
    assert res == " "

def test_capitilize_with_numbers():
    string_utils = StringUtils()
    res = string_utils.capitilize("123")
    assert res == "123"

def test_capitilize_with_spaces_in_string():
    string_utils = StringUtils()
    res = string_utils.capitilize("04 апреля 2023")
    assert res == "04 апреля 2023"

# Тесты для trim
def test_trim_positive():
    string_utils = StringUtils()
    res = string_utils.trim("   skypro")
    assert res == "skypro"

def test_trim_empty_string():
    string_utils = StringUtils()
    res = string_utils.trim("")
    assert res == ""

def test_trim_only_whitespace():
    string_utils = StringUtils()
    res = string_utils.trim("     ")
    assert res == ""

def test_trim_no_whitespace():
    string_utils = StringUtils()
    res = string_utils.trim("skypro")
    assert res == "skypro"

# Тесты для to_list
def test_to_list_default_delimiter():
    string_utils = StringUtils()
    res = string_utils.to_list("a,b,c,d")
    assert res == ["a", "b", "c", "d"]

def test_to_list_custom_delimiter():
    string_utils = StringUtils()
    res = string_utils.to_list("1:2:3", ":")
    assert res == ["1", "2", "3"]

def test_to_list_empty_string():
    string_utils = StringUtils()
    res = string_utils.to_list("")
    assert res == []

def test_to_list_with_whitespace():
    string_utils = StringUtils()
    res = string_utils.to_list(" a , b , c ")
    assert res == [" a ", " b ", " c "]

# Тесты для contains
def test_contains_positive_true():
    string_utils = StringUtils()
    res = string_utils.contains("SkyPro", "S")
    assert res == True

def test_contains_positive_false():
    string_utils = StringUtils()
    res = string_utils.contains("SkyPro", "U")
    assert res == False

def test_contains_empty_string():
    string_utils = StringUtils()
    res = string_utils.contains("", "S")
    assert res == False

def test_contains_empty_symbol():
    string_utils = StringUtils()
    res = string_utils.contains("SkyPro", "")
    assert res == True

def test_contains_with_numbers():
    string_utils = StringUtils()
    res = string_utils.contains("123", "2")
    assert res == True

# Тесты для delete_symbol
def test_delete_symbol_positive():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("SkyPro", "k")
    assert res == "SyPro"

def test_delete_symbol_substring():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("SkyPro", "Pro")
    assert res == "Sky"

def test_delete_symbol_empty_string():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("", "k")
    assert res == ""

def test_delete_symbol_not_found():
    string_utils = StringUtils()
    res = string_utils.delete_symbol("SkyPro", "X")
    assert res == "SkyPro"

# Тесты для starts_with
def test_starts_with_positive_true():
    string_utils = StringUtils()
    res = string_utils.starts_with("SkyPro", "S")
    assert res == True

def test_starts_with_positive_false():
    string_utils = StringUtils()
    res = string_utils.starts_with("SkyPro", "P")
    assert res == False

def test_starts_with_empty_string():
    string_utils = StringUtils()
    res = string_utils.starts_with("", "S")
    assert res == False

def test_starts_with_empty_symbol():
    string_utils = StringUtils()
    res = string_utils.starts_with("SkyPro", "")
    assert res == True

# Тесты для end_with
def test_end_with_positive_true():
    string_utils = StringUtils()
    res = string_utils.end_with("SkyPro", "o")
    assert res == True

def test_end_with_positive_false():
    string_utils = StringUtils()
    res = string_utils.end_with("SkyPro", "y")
    assert res == False

def test_end_with_empty_string():
    string_utils = StringUtils()
    res = string_utils.end_with("", "o")
    assert res == False

def test_end_with_empty_symbol():
    string_utils = StringUtils()
    res = string_utils.end_with("SkyPro", "")
    assert res == True

# Тесты для is_empty
def test_is_empty_true():
    string_utils = StringUtils()
    res = string_utils.is_empty("")
    assert res == True

def test_is_empty_whitespace():
    string_utils = StringUtils()
    res = string_utils.is_empty(" ")
    assert res == True

def test_is_empty_false():
    string_utils = StringUtils()
    res = string_utils.is_empty("SkyPro")
    assert res == False

def test_is_empty_with_content():
    string_utils = StringUtils()
    res = string_utils.is_empty("  content  ")
    assert res == False

# Тесты для list_to_string
def test_list_to_string_default_joiner():
    string_utils = StringUtils()
    res = string_utils.list_to_string([1,2,3,4])
    assert res == "1, 2, 3, 4"

def test_list_to_string_custom_joiner():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["Sky", "Pro"], "-")
    assert res == "Sky-Pro"

def test_list_to_string_empty_list():
    string_utils = StringUtils()
    res = string_utils.list_to_string([])
    assert res == ""

def test_list_to_string_single_element():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["Sky"])
    assert res == "Sky"

def test_list_to_string_with_whitespace():
    string_utils = StringUtils()
    res = string_utils.list_to_string(["a", "b"], " ")
    assert res == "a b"