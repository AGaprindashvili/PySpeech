import Resources.StaticTexts as st
import Resources.KnowledgeData as kd

# For behavior imports
import webbrowser
from datetime import datetime

class ConversationManager:

    def __init__(self, speechText, speechLanguage):
        self.speechText = speechText
        self.speechLanguage = speechLanguage

    def goConversation(content):
        txt = content.speechText.lower()
        lan = content.speechLanguage
        lanId = 1 if content.speechLanguage == "en" else 2
        try:
            behavior = kd.setBehavior(kd.getBehavior(txt, lanId), lan)
            return exec(behavior)
        except:
            pass