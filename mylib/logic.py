import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def wiki_search(name):
    """Search wikipedia for names"""
    results = wikipedia.search(name)
    return results


def phrase(name):
    """Return phrases from wikipedia"""
    page = wiki(name)
    blob = TextBlob(page)
    phrases = blob.noun_phrases
    return phrases
