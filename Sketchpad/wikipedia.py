import wikipedia
from hanziconv import HanziConv

class Wikipedia:
    def __init__(self):
        wikipedia.set_lang("zh-TW")
        self.hv = HanziConv()

    def random_content(self):
        rnd_title = wikipedia.random()
        content = wikipedia.summary(rnd_title, sentences=1)
        content = self.hv.toTraditional(content)
        rnd_title = self.hv.toTraditional(rnd_title)
        return (rnd_title, content)