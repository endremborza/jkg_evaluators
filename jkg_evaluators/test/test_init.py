from jkg_evaluators import __version__

def test_import():
    assert isinstance(__version__, str)
