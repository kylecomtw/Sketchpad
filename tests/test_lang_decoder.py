from unittest import TestCase
from unittest.mock import Mock
import logging
from Sketchpad.lang_decoder import LanguageDecoder
from Sketchpad.thought import Thought

logging.basicConfig()
logger = logging.getLogger("Sketchpad.test_lang_decoder")
logger.setLevel("INFO")

class LanguageDecoderTest(TestCase):
    def test_LanguageDecoder(self):
        props = [('語言', 'PartOf', '表達', '[[語言]] 是 [[表達]] 的一部分。', 2.0), 
            ('語言', 'MadeOf', '字母', '[[語言]] 可以用 [[字母]] 製成。', 2.0), 
            ('語言', 'PartOf', '生活', '[[語言]] 是 [[生活]] 的一部分。', 2.0), 
            ('語言', 'UsedFor', '聊天', '*[[聊天]] 的時候可能會用到 [[語言]]。', 2.8284),
            (' 語言', 'IsA', '溝通工具', '[[語言]] 是一種 [[溝通工具]]。', 2.0)]

        lang_decoder = LanguageDecoder()
        t1 = Thought()
        t1.intention = "pursue"
        t1.implicit = ("key", "關鍵詞")
        logger.info(lang_decoder.decode(t1))

        t2 = Thought()
        t2.intention = "spread"
        t2.wm = props
        t2.implicit = ("assoc", '書本'])
        logger.info(lang_decoder.decode(t2))

        t3 = Thought()
        t3.intention = "psychoanalysis"
        t3.implicit = ("key", "關鍵詞")
        logger.info(lang_decoder.decode(t3))

        t4 = Thought()
        t4.intention = "elicit"
        t4.implicit = ("random", ("標題", "隨機內文"))
        logger.info(lang_decoder.decode(t4))