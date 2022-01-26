import speech_recognition as sr
import Resources.StaticTexts as st

class RecognitionManager:

    def __init__(self, languageType):
        self.languageType = languageType

    def goRecognition(param):
        spReorg = sr.Recognizer()
        with sr.Microphone() as spSource:
            spAudio = spReorg.listen(spSource)
            try:
                return spReorg.recognize_google(spAudio, language = param.languageType)
            except:
                return st.loadText(2, param.languageType)