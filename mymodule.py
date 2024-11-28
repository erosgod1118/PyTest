def something():
    """a doctest in a docstring
    >>> something()
    42
    """
    return 42

def test_random(y):
    """
    >>> random.random() # doctest: +SKIP
    0.156231223

    >>> 1 + 1
    2
    """