import pytest
from scripts.encontrando_letra_a import count_letter_a

def test_word_without_letter_a():
    assert count_letter_a('hello') == 0

def test_word_1_lowercase_letter_a():
    assert count_letter_a('technical') == 1

def test_word_2_lowercase_letters_a():
    assert count_letter_a('actually') == 2

def test_word_with_1_letter_a_lowercase_e_1_uppercase():
    assert count_letter_a('Ana') == 2

def test_word_2_capital_letters_a():
    assert count_letter_a('AnA') == 2

def test_sentence_with_4_letters_in_lower_case():
    assert count_letter_a('Today is a very beautiful day') == 4

def test_sentence_with_2_lowercase_letters_and_2_capital_letters():
    assert count_letter_a('TodAy is a very beAutiful day') == 4

def test_sentence_with_2_lowercase_letters():
    assert count_letter_a('TodAy is A very beAutiful dAy') == 4

def test_sentence_without_letter_a():
    assert count_letter_a('Hello World') == 0

def test_word_1_capital_letter_a():
    assert count_letter_a('All') == 1
