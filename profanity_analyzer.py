from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata
import nltk
import os
from profanity_filter import ProfanityFilter

class ProfanityAnalyzer(Component):
    """A pre-trined sentiment component"""
    name = "prfanity_nanlyzer"
    provides = ["entitties"]
    requires = []
    defaults = {}
    language_list = ["en"]

    def __init__(self,component_config=None) -> None:
        super(ProfanityAnalyzer,self).__init__(component_config)
    
    # def train(self, training_data, cfg, **kwargs):


    def convert_to_rasa(self, value, confidence):
        """Convert model output into the Rasa NLU compatible output format."""
        return { "value":value,
                    "confidence":confidence,
                    "entity":"profane_word",
                    "extractor":"profanity_extractor" }

    def process(self, message, **kwargs):
        pf = ProfanityFilter()
        text = message.txt
        # text = "This is shit" == True | False if True
        value = "na"
        confidence = "0"
        if pf.is_profane(text):
            token = text.split(" ")
            for token in token:
                if pf.is_profane(token):
                    value = token
                    confidence = 100
        if value != "na":
            entity = self.convert_to_rasa(value,confidence)
            message.set("entities",[entity],add_to_output=True)
        else:
            pass

    # def persist(self, model_dir):
    