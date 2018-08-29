import re
from .thought import Thought
from .scripts import script_templates
import numpy as np


class LanguageDecoder:
    def __init__(self):
        pass
    
    def decode(self, thought):
        intention = thought.intention
        props = thought.wm
        implicit = thought.implicit
        if intention == "pursue":
            resp = self.decode_pursue(props, implicit)
        elif intention == "spread":
            resp = self.decode_spread(props, implicit)
        elif intention == "psychoanalysis":
            resp = self.decode_psychoanalysis(props, implicit)
        elif intention == "elicit":
            resp = self.decode_random(props, implicit)
        else:
            resp = "..."
        return resp

    def decode_pursue(self, props, impl):        
        key, title, content = impl[1]
        templ = self.load_template("pursue")
        return templ.format(key = key, title=title, content=content)

    def decode_spread(self, props, impl):              
        assoc = impl[1]
        respText = props[0][0]      
        i = 0          
        for prop_x in props:      
            if not isinstance(prop_x[3], str): continue
            text = prop_x[3]
            text = text.replace("[[%s]]" % (prop_x[0]), "")
            text = re.sub(r"[\[\]\s*]", "", text)
            text = text.replace("。", "，")
            if i > 0 and i % 2 == 0: respText += self.load_template("connectives")        
            respText += text
            i += 1
        respText = self.load_template("spread").format(key=assoc) + respText
        return respText
    
    def decode_psychoanalysis(self, props, impl):
        key = impl[1]        
        templ = self.load_template("psychoanalysis")
        return templ.format(key = key)
    
    def decode_random(self, props, impl):
        title, content = impl[1]        
        templ = self.load_template("random")
        return templ.format(title=title, content=content)
    
    def load_template(self, category):
        templ_list = script_templates.get(category, [])
        idx = np.random.choice(np.arange(len(templ_list)), 1)
        templ = templ_list[idx[0]]
        return templ