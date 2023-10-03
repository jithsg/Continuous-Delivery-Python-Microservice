import wikipedia


def wiki(name='War Goddess', length=1):
    """Return a summary from Wikipedia."""
    return wikipedia.summary(name, sentences=length)


def search(name='War Goddess'):
    """Return a list of Wikipedia search results."""
    return wikipedia.search(name)
