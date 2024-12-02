import pytest

# def test_hello(pytester):
#     pytester.makeconftest(
#         """
#         import pytest 

#         @pytest.fixture(params=[
#             "Briana",
#             "Andreas",
#             "Floris",
#         ])
#         def name(request):
#             return request.param
#         """
#     )

#     pytester.makepyfile(
#         """
#         def test_hello_default(hello):
#             assert 1
#         """
#     )

#     result = pytester.runpytest()
#     result.assert_outcomes(passed=1)

def test_hello_default(hello):
    assert hello() == "Hello World"

def test_hello_name(hello, name):
    assert hello(name) == "Hello {0}".format(name)