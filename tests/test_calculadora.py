﻿import pytest
from src.calculadora import soma, sub, mul, div

def test_soma():
    assert soma(2, 3) == 5

def test_sub():
    assert sub(5, 2) == 3

def test_mul():
    assert mul(3, 4) == 12

def test_div():
    assert div(10, 2) == 5

def test_div_zero():
    with pytest.raises(ValueError):
        div(1, 0)
