import pytest
from scripts.sequencia_fibonacci import fibonacci_sequence_number

def test_one():
    assert fibonacci_sequence_number(1) == True

def test_two():
    assert fibonacci_sequence_number(2) == True

def test_three():
    assert fibonacci_sequence_number(3) == True

def test_four():
    assert fibonacci_sequence_number(4) == False

def test_five():
    assert fibonacci_sequence_number(5) == True

def test_six():
    assert fibonacci_sequence_number(6) == False

def test_seven():
    assert fibonacci_sequence_number(7) == False

def test_eight():
    assert fibonacci_sequence_number(8) == True

def test_nine():
    assert fibonacci_sequence_number(9) == False

def test_ten():
    assert fibonacci_sequence_number(10) == False

def test_float():
    assert fibonacci_sequence_number(1.23) == False

def test_float():
    assert fibonacci_sequence_number(-1) == False