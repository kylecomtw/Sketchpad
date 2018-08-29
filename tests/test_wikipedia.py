from unittest import TestCase
from unittest.mock import Mock
import logging
from Sketchpad.wikipedia import Wikipedia

logging.basicConfig()
logger = logging.getLogger("Sketchpad.test_wikipedia")
logger.setLevel("INFO")

class WikipediaTest(TestCase):
    def test_Wikipedia(self):
        wiki = Wikipedia()
        logger.info(wiki.random_content())