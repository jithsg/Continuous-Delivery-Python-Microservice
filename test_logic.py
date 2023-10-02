
from mylib.logic import wiki



def test_wiki():
    """Test the wiki() function."""
    result = wiki('War Goddess', 2)
    assert 'god' in result
    assert 'Aphrodite' not in result


    