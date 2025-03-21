import pytest

@pytest.fixture
def numbers():
    a = 10
    b = 20
    c = 25
    return [a,b,c]

@pytest.mark.xfail
def test_m1(numbers):
    x = 15
    assert numbers[0] == x

@pytest.mark.skip
def test_m2(numbers):
    y = 20
    assert numbers[1] == y

def test_m3(numbers):
    z = 25
    assert numbers[2] == z


