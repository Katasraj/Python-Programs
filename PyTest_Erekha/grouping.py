class TestClass:
    def test_one(self):
        x = 'Error'
        assert 'r' in x

    def test_two(self):
        x = "Hello"
        assert hasattr(x,"check")