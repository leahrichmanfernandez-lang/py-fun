import pytest
from src.calculator.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add_numbers_and_languages(calc):
    assert calc.add("1", "1.600") == pytest.approx(2.6)
    assert calc.add("three", "1.600") == pytest.approx(4.6)
    assert calc.add("cinco", "siete") == 12
    assert calc.add("семь", "восемь") == 15
    assert calc.add("III", "   VIII") == 11
    assert calc.add("三", "五") == 8
    assert calc.add("0", "X") == 10
    assert calc.add("ocho", "nueve") == 17

def test_sub_mul_div(calc):
    assert calc.sub("ocho", "nueve") == -1
    assert calc.mul("ocho", "nueve") == 72
    assert calc.div("ocho", "dos") == 4.0

def test_factorize(calc):
    assert calc.factorize("три") == [3]
    assert calc.factorize("X") == [2, 5]
    assert calc.factorize("ocho") == [2, 2, 2]
    assert calc.factorize(3 + 5) == [2, 2, 2]
    assert calc.factorize(27) == [3, 3, 3]
    assert calc.factorize(1092) == [2, 2, 3, 7, 13]
    assert calc.factorize(32768) == [2] * 15
    assert calc.factorize(10952347) == [7, 23, 59, 1153]
    assert calc.factorize(100000039) == [100000039]

def test_invalid_input(calc):
    with pytest.raises(ValueError):
        calc.add("invalid", "1")
