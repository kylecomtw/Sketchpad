import requests
import requests_cache
import asyncio
import config
import numpy as np
import re
from hanziconv import HanziConv

requests_cache.install_cache('ltm_cache')

class LongTermMemory:
    def __init__(self):
        self.hv = HanziConv()

    def retrieve(self, lemmas): 
        rel_list = []
        for lemma_x in lemmas:
            rel_list += self.query_concept_net(lemma_x)
            # rel_list += self.query_babel_net(lemma_x)
        
        return rel_list

    def query_concept_net(self, lemma):
        cnet_url = "http://api.conceptnet.io/c/zh/{lemma}"
        resp = requests.get(cnet_url.format(lemma=lemma))
        if resp.status_code != 200:
            return []
        jobj = resp.json()
        edges = jobj.get("edges", {})

        rel_list = []        
        for edge_x in edges:
            start_label = edge_x.get("start", {}).get("label", "")
            end_label = edge_x.get("end", {}).get("label", "")
            rel_label = edge_x.get("rel", {}).get("label", "")            
            surface_text = edge_x["surfaceText"]
            if not surface_text: continue
                
            if len(re.findall("[a-zA-Z]", surface_text)) > 1:
                continue

            rel = (start_label, rel_label, end_label,
                    surface_text)
            rel_list.append(rel)
        weights = np.array([x.get("weight", 0) for x in edges])
        probs = weights / np.sum(weights)        

        if rel_list:
            sel_indices = np.random.choice(len(rel_list), min(5, len(rel_list)), False, probs)
            rel_list = [rel_list[x] for x in sel_indices]
        
        return rel_list

    def query_babel_net(self, lemma):
        lemma_simp = self.hv.toSimplified(lemma)
        bn_sense_url = "https://babelnet.io/v5/getSenses?" + \
                       "lemma={lemma}&searchLang=ZH&key={key}".format(
                           lemma=lemma_simp, key=config.BABELNET_KEY
                       )
        resp = requests.get(bn_sense_url)
        if resp.status_code != 200:
            logger.error("Error when retrieving bn_sense")
            logger.error(resp.status_code, resp.content)
            return []
        
        synset_list = []
        sense_obj = resp.json()
        for sense_x in sense_obj:            
            synset = sense_x.get("properties", {}).get("synsetID", {})
            if synset.get("id", "") in synset_list: continue

            if not synset or synset["pos"] != "NOUN":
                continue
            synset_list.append(synset["id"])

        sense_weights = 1/(np.arange(len(synset_list))+1) * 2
        sense_probs = sense_weights / np.sum(sense_weights)
        synset_pick = np.random.choice(synset_list, 3, False, sense_probs)
        
        return synset_pick.tolist()
