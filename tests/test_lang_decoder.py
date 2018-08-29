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
        props = [('知識', 'Causes', '財富', '[[知識]] 可能會帶來 [[財富]]。'), 
            ('讀書', 'Causes', '知識', '[[讀書]] 可能會帶來 [[知識]]。'), 
            ('書本', 'MadeOf', '知識', '[[書本]] 可以用 [[知識]] 製成。'), 
            ('上課', 'Causes', '知識', '[[上課]] 可能會帶來 [[知識]]。'), 
            ('唸書', 'Causes', '知識', '[[唸書]] 可能會帶 來 [[知識]]。')]

        lang_decoder = LanguageDecoder()
        t1 = Thought()
        t1.intention = "pursue"
        t1.implicit = ("key", "關鍵詞")
        logger.info(lang_decoder.decode(t1))

        t2 = Thought()
        t2.intention = "spread"
        t2.wm = props
        t2.implicit = ("assoc", ['書本', '讀書', '上課', '財富', '唸書'])
        logger.info(lang_decoder.decode(t2))

        t3 = Thought()
        t3.intention = "psychoanalysis"
        t3.implicit = ("key", "關鍵詞")
        logger.info(lang_decoder.decode(t3))

        t4 = Thought()
        t4.intention = "elicit"
        t4.implicit = ("random", ("標題", "隨機內文"))
        logger.info(lang_decoder.decode(t4))