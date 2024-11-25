import pytest 

@pytest.fixture(params=[10, pytest.param(11, marks=pytest.mark.skip)])
def data_set(request):
    return request.param 

def test_data(data_set):
    pass