from src.math_operations import add, sub

def test_add():
    assert add(1,2) == 3
    assert add(5,8) == 13

def test_sub():
    assert sub(1,2) == -1
    assert sub(5,8) == -3    