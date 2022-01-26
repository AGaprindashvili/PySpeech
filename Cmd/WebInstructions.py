import webbrowser
import validators
import os

def openBrowser(url):
    try:
        chromePath = "C://Program Files (x86)//Google//Chrome//Application//chrome.exe"
        if os.path.isfile(chromePath) == False:
            chromePath = "C://Program Files//Google//Chrome//Application//chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))
        if validators.url("http://" + url):
            return "webbrowser.get(\"chrome\").open(\"" + url + "\")"
        else:
            return "webbrowser.get(\"chrome\").open(\"http://google.com/search?q=" + url + "\")"
    except:
        return "webbrowser.open(\"" + url + "\")"