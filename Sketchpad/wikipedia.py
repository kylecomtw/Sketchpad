import wikipedia
import random
import requests_cache
from hanziconv import HanziConv

class Wikipedia:
    def __init__(self):
        wikipedia.set_lang("zh-TW")
        random.seed()
        self.hv = HanziConv()

    def random_content(self):
        with requests_cache.disabled():
            rnd_title = wikipedia.random()
        content = wikipedia.summary(rnd_title, sentences=1)
        content = self.hv.toTraditional(content)
        rnd_title = self.hv.toTraditional(rnd_title)
        return (rnd_title, content)