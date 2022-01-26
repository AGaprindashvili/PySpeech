from gtts import gTTS
from playsound import playsound
import os

class SpeechManager:

    def __init__(self, speechText, languageType):
        self.speechText = speechText
        self.languageType = languageType

    def goSpeech(spText):
        try:
            spFile = "spvoicefile.mp3"
            spVoice = gTTS(text = spText.speechText, lang = spText.languageType, slow = False)
            spVoice.save(spFile)
            playsound(spFile)
            os.remove(spFile)
        except:
            pass