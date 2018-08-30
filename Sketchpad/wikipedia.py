import wikipedia
import random
import requests_cache
from wikipedia.exceptions import DisambiguationError
from hanziconv import HanziConv
import logging
logger = logging.getLogger("Sketchpad.wikipedia")
logger.setLevel("INFO")

class Wikipedia:
    def __init__(self):
        wikipedia.set_lang("zh-TW")
        random.seed()
        self.hv = HanziConv()

    def search(self, title):

        content = None                
        for i in range(3):
            try:
                content = wikipedia.summary(title, sentences=1)
            except DisambiguationError as ex:                
                logger.warning("Disambiguation error when finding summary, try searching")
                title = ex.options[0]

        if not content:
            raise Exception("Search failed in Wikipedia")
        title = self.hv.toTraditional(title)
        content = self.hv.toTraditional(content)
        return title, content

    def random_content(self):
        for i in range(5):
            try:
                with requests_cache.disabled():
                    rnd_title = wikipedia.random()
                    break
            except DisambiguationError:
                logger.warning("Disambiguation error in wiki.random, retry %d", i)                
        content = wikipedia.summary(rnd_title, sentences=1)
        content = self.hv.toTraditional(content)
        rnd_title = self.hv.toTraditional(rnd_title)
        return (rnd_title, content)