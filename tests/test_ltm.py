from unittest import TestCase
from unittest.mock import Mock
import logging
from Sketchpad.ltm import LongTermMemory

logging.basicConfig()
logger = logging.getLogger("Sketchpad.test_ltm")
logger.setLevel("INFO")

class LtmTest(TestCase):
    def test_ltm(self):
        ltm = LongTermMemory()
        rel_list = ltm.retrieve(["語言"])
        logger.info(rel_list)