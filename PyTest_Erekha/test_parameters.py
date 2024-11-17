import pytest

@pytest.mark.parametrize('x,y,z',[(10,20,200),(20,40,800)])
def test_mp(x,y,z):
    assert x*y == z
