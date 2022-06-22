from typing import Any, Text, Dict, List ##Datatypes

from rasa_sdk import Action, Tracker ##
from rasa_sdk.executor import CollectingDispatcher

class action_search(Action):

    def name(self) -> Text:
        return "action_search"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        dispatcher.utter_message("Here are your search results")
        return []

class action_ShowLatestNews(Action):

    def name(self) -> Text:
        return "action_ShowLatestNews"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text,Any]]:
        dispatcher.utter_message("Here are the latest news for your category")
        return []
