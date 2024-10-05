import pytest
import os
import sys
from src.main import add, subtract

# Добавляем путь к пакету src в системный путь Python
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))


def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2

def test_subtract():
    assert subtract(2, 1) == 1
    assert subtract(-1, 1) == -2
    assert subtract(-1, -1) == 0
