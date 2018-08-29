from unittest import TestCase, skip
from unittest.mock import Mock
import logging
from Sketchpad import WanderEngine
import json

logging.basicConfig()
logger = logging.getLogger("Sketchpad.test_wander_engine")
logger.setLevel("INFO")

class WanderEngineTest(TestCase):
    @skip("1")
    def test_WanderEngine(self):
        we = WanderEngine()
        nns = we.get_noun_compounds("這台咖啡電腦有蘋果鉛筆")
        logger.info("Noun Compounds: ")        
        logger.info(nns)
        self.assertTrue(all([x in nns for x in ("咖啡電腦", "蘋果鉛筆")]))     
    
    @skip("2")
    def test_nn_weight(self):
        we = WanderEngine()
        nns = ["電腦", "咖啡電腦", "鉛筆", "學生"]
        w = we.get_nns_weightings(nns)
        logger.info("weights: %s", w)
        samples = we.sample_nns(nns, w, 2)
        logger.info(samples)
    
    def test_wander(self):
        we = WanderEngine()
        respText, memory = we.wander("這省")
        logger.info(respText)
        respText, memory = we.wander(respText, memory)
        logger.info(respText)
        respText, memory = we.wander(respText, memory)
        logger.info(respText)