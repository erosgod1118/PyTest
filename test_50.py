import pytest 

@pytest.mark.parametrize("i", range(50))
def test_sum(i):
    if i in (17, 25):
        pytest.fail("bad luck")