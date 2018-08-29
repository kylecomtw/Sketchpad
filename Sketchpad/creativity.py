from .thought import Thought
from .wikipedia import Wikipedia
import numpy as np
import logging

logger = logging.getLogger("Sketchpad.Creativity")
wiki = Wikipedia()
np.random.seed()

class Creativity:
    def __init__(self, props, memory):
        self.props = props
        self.memory = memory

    def diversify(self):
        
        self.forget()
        trace = self.memory["trace"]
        current_word = self.memory["working"]
        if current_word in trace: trace.remove(current_word)
        trace.append(current_word)
        self.memory["trace"] = trace

        if not self.props:
            thought = self.pursue()
        else:
            strategies = [
                self.pursue, self.spread, self.random]
            weights = np.array([1,2,0.1])        
            strategy_func = np.random.choice(strategies, 1, 
                False, weights/np.sum(weights)).tolist() 
            logger.info("strategy selected: ")
            logger.info(strategy_func[0].__name__)
            thought = strategy_func[0]()
                
        thought.wm = self.props
        
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
        if not memory:            
            thought = self.spread()
        else:
            trace = self.memory.get("trace", []).copy()
            visited_list = self.memory.get("visited", [])
            
            for visited in visited_list:
                if visited in trace:
                    trace.remove(visited)

            trace_weights = np.arange(len(trace)) + 1
            trace_prob = trace_weights / np.sum(trace_weights)
            pick = self.pick_object(trace, 1)[0]            
            title, content = wiki.search(pick)
            thought.implicit = ("elicit", (pick, title, content))
            thought.intention = "pursue"
            
            visited_list.append(pick)            
            logger.info("Visited: %s", visited_list)
            self.memory["visited"] = visited_list
        return thought
    
    def spread(self):
        """ spread across other possibilities
        """        
        thought = Thought()

        # assoc_set is no use for now
        assoc_set = set()
        for prop_x in self.props:
            assoc_set.add(prop_x[0])
            assoc_set.add(prop_x[2])            
        assoc_set = assoc_set.difference()        

        thought.implicit = ("assoc", self.memory["working"])
        thought.intention = "spread"
        return thought
    
    def psychoanalysis(self):
        """ repeat the keywords
        """    
        thought = Thought()
        current_word = self.pick_object(self.memory.get("working", []), 1)
        thought.implicit = ("key", current_word[0])
        thought.intention = "psychoanalysis"
        return thought

    def random(self):
        """ repeat the keywords
        """            
        title, content = wiki.random_content()
        thought = Thought()
        thought.intention = "elicit"
        thought.implicit = ("elicit", (title, content))
        return thought

    def pick_object(self, x, n=1):
        if len(x):
            idx_list = np.arange(len(x))
            picks = np.random.choice(idx_list, min(n, len(x)))
            return [x[i] for i in picks]
        else:
            return []