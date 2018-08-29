from os.path import abspath, dirname, join
import logging
import math
from itertools import groupby
import json
import pickle
import jieba.posseg as pseg
import numpy as np
from .thought import Thought

logger = logging.getLogger("Sketchpad.WanderEngine")

class WanderEngine:
    def __init__(self):
        basepath = dirname(abspath(__file__))
        try:
            with open(join(basepath, "../data/as_wordFreq.pickle"), "rb") as fin:
                self.word_freq = pickle.load(fin)
        except Exception as ex:
            logger.error(ex)
            self.word_freq = {}        

    def wander(self, intext, memoryStr=""):
        try:
            memory = json.loads(memoryStr)
        except:
            memory = {}
                
        nns = self.get_noun_compound(intext)
        weights = self.get_nns_weightings(nns)
        keywords = self.sample_nns(nns, weights, n=2)
        
        memory["working"] = keywords
        ltm = LongTermMemory()
        props = ltm.retrieve(keywords)
        creativity = Creativity(props, memory)
        thought = creativity.diversify()  # type: Thought        
        memoryJson = json.dumps(creativity.memory)

        return thought, memoryJson
    
    def get_noun_compounds(self, intext):
        wds = pseg.cut(intext)        
        grps = groupby(wds, key=lambda x: x.flag)
        noun_grps = filter(lambda x: x[0]=="n", grps)
        nns = map(lambda x: "".join([tok.word for tok in x[1]]), noun_grps)
        return list(nns)
    
    def get_nns_weightings(self, nns):
        nn_freq = [self.word_freq.get(x, 1) for x in nns]
        nn_weights = [1/(math.log(f)+1) for f in nn_freq]
        return nn_weights
    
    def sample_nns(self, nns, weights, n=1):
        probs = weights / np.sum(weights)
        return np.random.choice(nns, n, False, probs)
