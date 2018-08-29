import unittest
import logging

logger = logging.getLogger("Sketchpad")
ch = logging.StreamHandler()
ch.setLevel("INFO")
formatter = logging.Formatter("[%(levelname)s] %(name)s: %(message)s")
ch.setFormatter(formatter)
logger.addHandler(ch)

if __name__ == "__main__":
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest()
    runner = unittest.TextTestRunner()
    runner.run(suite)
