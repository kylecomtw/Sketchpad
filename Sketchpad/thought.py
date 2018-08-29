
class Thought:
    def __init__(self):
        self.verbal = ""
        self.intention = ""
        self.wm = {}
        self.implicit = {}
        self.action = {}
        self.sensory = {}   

    def __repr__(self):     
        if self.implicit or self.action or self.sensory:
            return "<Thought with wander: %s, %s>" % (self.verbal, self.implicit)
        else:
            if self.verbal:
                return "<Thought: %s>" % self.verbal
            else:
                return "<Thought with no content>"
