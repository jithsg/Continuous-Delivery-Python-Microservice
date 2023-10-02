import wikipedia


def wiki(name='War Goddess', length=1):
    """Return a summary from Wikipedia."""
    return wikipedia.summary(name, sentences=length)
