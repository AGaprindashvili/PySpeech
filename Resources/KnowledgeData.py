from Modules.SpeechManager import SpeechManager
from Modules.RecognitionManager import RecognitionManager
import Resources.StaticTexts as st
import Cmd.WebInstructions as cmdWeb
import sqlite3

# For behavior imports
from datetime import datetime

def speechListen(spText, spLan):
    setSpeech = SpeechManager(spText, spLan)
    setSpeech.goSpeech()
    setRecognition = RecognitionManager(spLan)
    return setRecognition.goRecognition()

def getBehavior(thing, lan):
    try:
        setResult = "void"
        conn = sqlite3.connect("knowledge.db")
        c = conn.cursor()
        result = c.execute(
        "SELECT behavior FROM actions WHERE enabled = 1 AND lan = ? AND thing LIKE ? LIMIT 1", (lan, '%' + thing + '%')
        ).fetchone()
        if result is not None:
            setResult = result[0]
        c.close()
        conn.close()
        return setResult
    except Exception as e:
        return "void"

def setBehavior(action, lan):

    if action == "void":
        dialog = st.loadText(6, lan)
        print(dialog)
        setSpeech = SpeechManager(dialog, lan)
        setSpeech.goSpeech()
        action = "pass"

    elif action == "webbrowser.open":
        dialog = st.loadText(5, lan)
        print(dialog)
        dialog = speechListen(dialog, lan)
        print(dialog)
        action = cmdWeb.openBrowser(dialog)

    elif action == "datetime.now.time":
        dialog = st.loadText(7, lan) + datetime.now().strftime("%H:%M")
        print(dialog)
        setSpeech = SpeechManager(dialog, lan)
        setSpeech.goSpeech()
        action = "pass"

    else:
        print(action)
        setSpeech = SpeechManager(action, lan)
        setSpeech.goSpeech()
        action = "pass"

    return action