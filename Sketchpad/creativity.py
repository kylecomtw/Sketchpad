from .thought import Thought
from .wikipedia import Wikipedia
import numpy as np
import logging

logger = logging.getLogger("Sketchpad.Creativity")

class Creativity:
    def __init__(self, props, memory):
        self.props = props
        self.memory = memory

    def diversify(self):
        strategies = [
            self.pursue, self.spread, self.psychoanalysis, 
            self.random]
        weights = np.array([1,1,1,0.1])        
        strategy_func = np.random.choice(strategies, 1, 
            False, weights/np.sum(weights)).tolist() 
        logger.info("strategy selected: ")
        logger.info(strategy_func)
        thought = strategy_func[0]()
        # thought = self.spread()

        self.forget()
        self.memory["trace"] += self.memory["working"]
        return thought
    
    def forget(self):
        ngen = self.memory.get("ngen", 0)
        trace = self.memory.get("trace", [])
        if len(trace) > 5:
            trace = trace[1:]

        self.memory["trace"] = trace

    def pursue(self):
        """ pursue in the memory trace
        """
        memory = self.memory
        props = self.props
        thought = Thought()
        if not memory or not memory.get("trace", []):            
            prop_x = self.pick_object(props, 1)
            thought.implicit = ("prop", prop_x[0])
        else:
            trace = self.memory.get("trace", [])            
            trace_prob = np.arange(len(trace)) / np.sum(np.arange(len(trace)))
            pick = self.pick_object(trace, 1)[0]            
            thought.implicit = ("key", pick)
        thought.intention = "pursue"
        return thought
    
    def spread(self):
        """ spread across other possibilities
        """        
        thought = Thought()
        prop_x = self.pick_object(self.props, 1)
        thought.implicit = ("prop", prop_x[0])
        thought.intention = "spread"
        return thought
    
    def psychoanalysis(self):
        """ repeat the keywords
        """    
        thought = Thought()
        current_word = self.pick_object(self.memory.get("working", []), 1)
        thought.implicit = ("key", current_word)
        thought.intention = "psychoanalysis"
        return thought

    def random(self):
        """ repeat the keywords
        """    
        wiki = Wikipedia()
        title, content = wiki.random_content()
        thought = Thought()
        thought.intention = "elicit"
        thought.implicit = ("random", (title, content))
        return thought

    def pick_object(self, x, n=1):
        if len(x):
            idx_list = np.arange(len(x))
            picks = np.random.choice(idx_list, min(n, len(x)))
            return [x[i] for i in picks]
        else:
            return []