from unittest import TestCase
from unittest.mock import Mock
import logging
from Sketchpad.creativity import Creativity

logging.basicConfig()
logger = logging.getLogger("Sketchpad.test_creativity")
logger.setLevel("INFO")

class CreativityTest(TestCase):
    def test_creativity(self):
        
        props = [('知識', 'Causes', '財富', '[[知識]] 可能會帶來 [[財富]]。'), 
            ('讀書', 'Causes', '知識', '[[讀書]] 可能會帶來 [[知識]]。'), 
            ('書本', 'MadeOf', '知識', '[[書本]] 可以用 [[知識]] 製成。'), 
            ('上課', 'Causes', '知識', '[[上課]] 可能會帶來 [[知識]]。'), 
            ('唸書', 'Causes', '知識', '[[唸書]] 可能會帶 來 [[知識]]。')]
        cr = Creativity(props, {"working": ["知識"]})
        thought = cr.diversify()
        logger.info(thought)

        crm = Creativity(props, {
            "working": ["知識"],
            "trace": ["知識", "學問", "成績", "財富"]})
        thought = crm.diversify()
        logger.info(thought)