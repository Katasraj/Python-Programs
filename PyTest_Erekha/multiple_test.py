import pytest

@pytest.mark.one       # py.test -m one
def test_method1():
    x = 5
    y = 10
    assert x == y

@pytest.mark.two    #py.test -m two
def test_method2():
    a = 15
    b = 20
    assert a+5 == b


# py.test -k method1 -v
# py.test -k method2 -v

