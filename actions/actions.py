# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


projects = {"covid": "https://github.com/d33pster/COVID-19-DL-ChestXray",
            "WebRep": "https://github.com/d33pster/WebRep",
            "PSSQL-auto": "https://github.com/d33pster/PSSQL-auto",
            "d33pster-chatbot": "https://github.com/d33pster/d33pster-chatbot"}

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_projects"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        for key in projects:
            if key=='covid':
                output = "Deep Learning Based COVID-19 detection using chest Xrays: " + projects[key]
                dispatcher.utter_message(text=output) 
            elif key=='WebRep':
                output = "WebRep ~ A cross platform python app to recon a website/webapp: " + projects[key]
                dispatcher.utter_message(text=output) 
            elif key=='PSSQL-auto':
                output = "PSSQL-auto ~ A cross platform python app to process Big Data: " + projects[key]
                dispatcher.utter_message(text=output) 
            elif key=='d33pster-chatbot':
                output = "Me: " + projects[key]
                dispatcher.utter_message(text=output)
            else:
                pass
                
        return []
