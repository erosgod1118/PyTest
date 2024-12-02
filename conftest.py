import pytest 

pytest_plugins = ["pytester"]

def pytest_addoption(parser):
    group = parser.getgroup("helloworld")
    group.addoption(
        "--hname",
        action="store",
        dest="name",
        default="World",
        help='Default "name" for hello().',
    )

@pytest.fixture
def hello(request):
    name = request.config.getoption("name")

    def _hello(name=None):
        if not name:
            name = request.config.getoption("name")
        return f"Hello {name}"
    
    return _hello

@pytest.fixture(params=[
    "Brianna",
    "Andreas",
    "Floris",
])
def name(request):
    return request.param