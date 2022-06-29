from typing import Any, Text, Dict, List ##Datatypes
import re

from rasa_sdk import Action, Tracker ##
from rasa_sdk.executor import CollectingDispatcher

class action_search(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        camera = tracker.get_slot('camera')
        ram = tracker.get_slot('RAM')
        battery = tracker.get_slot('battery')

        dispatcher.utter_message("Here are your search results")
        dispatcher.utter_message("The features you entered: camera:" + str(camera) + ", ram:" + str(ram) + "and battery:" + str(battery))
        return []

class action_ShowLatestNews(Action):

    def name(self) -> Text:
        return "action_ShowLatestNews"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        dispatcher.utter_message("Here are the latest news for your category")
        return []

class product_search_form(FormAction):
    """Example of custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""
        return "product_search_form"
    
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["ram","camera","battery","budget"]
    
    def validate_ram(self, value: Text, dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: Dict[Text,Any]) -> Dict[Text, Any]:
        """Validate num of ram value"""

        ram_int = int(re.findall(r'[0-9+',value[0]))
        if ram_int < 50 :
            return {"ram":ram_int}
        else:
            dispatcher.utter_message(template="utter_wrong_ram")
        return {"ram":None}
    
    def validate_camera(self, value: Text, dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: Dict[Text,Any]) -> Dict[Text, Any]:
        """Validate num of camera value"""

        camera_int = int(re.findall(r'[0-9+',value[0]))
        if camera_int < 150 :
            return {"camera":camera_int}
        else:
            dispatcher.utter_message(template="utter_wrong_camera")
        return {"camera":None}

    def validate_budget(self, value: Text, dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: Dict[Text,Any]) -> Dict[Text, Any]:
        """Validate num of budget value"""

        budget_int = int(re.findall(r'[0-9+',value[0]))
        if budget_int < 5000 :
            return {"budget":budget_int}
        else:
            dispatcher.utter_message(template="utter_wrong_budget")
        return {"budget":None}

    def validate_battery(self, value: Text, dispatcher: CollectingDispatcher,
        tracker: Tracker, domain: Dict[Text,Any]) -> Dict[Text, Any]:
        """Validate num of battery value"""

        battery_int = int(re.findall(r'[0-9+',value[0]))
        if battery_int > 2500  :
            return {"battery":battery_int}
        else:
            dispatcher.utter_message(template="utter_wrong_ram")
        return {"battery":None}

    def submit(seld, dspatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:
        dispatcher.utter_message("Please find your searched items here .........")
        
        return {}