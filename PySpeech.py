from Modules.SpeechManager import SpeechManager
from Modules.RecognitionManager import RecognitionManager
from Modules.ConversationManager import ConversationManager
import Resources.StaticTexts as st

def letListen(lan):
    print(st.loadText(4, lan))
    setRecognition = RecognitionManager(lan)
    return setRecognition.goRecognition()

def letSpeech(speechText, lan, goWork):
    print(speechText)
    setConversation = ConversationManager(speechText, lan)
    spText = setConversation.goConversation() if goWork else speechText
    setSpeech = SpeechManager(spText, lan)
    setSpeech.goSpeech()

def listenAndSpeech(lan):
    letSpeech(letListen(lan), lan, True)

def selectLanguage(lan):
    letSpeech(st.loadText(1, lan), lan, False)
    languages = {"1": "en", "2": "ru"}
    getLan = letListen(lan)
    if getLan in languages:
        return languages[getLan]
    else:
        return selectLanguage(lan)

def letStart(language):
    if letListen(language).lower() == "ok":
        letSpeech(st.loadText(0, language), language, False)
        language = selectLanguage(language)
        letSpeech(st.loadText(3, language), language, False)
        while True:
            listenAndSpeech(language)
    else:
        letStart(language)

print("Say: ok")
letStart("en")