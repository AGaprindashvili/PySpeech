def loadText(id, lan):
    try:
        if lan == "en":
            switcher = {
                0: "Hello my creative programmer!",
                1: "Please select a language. For English say: 1 - For Russian say: 2",
                2: "I don't understand something, can you repeat?",
                3: "English language is chosen! How can I help you?",
                4: "Listening...",
                5: "I open the browser, tell me the address",
                6: "Sorry! I don't understand something, can you repeat?",
                7: "The current time is ",
            }
        if lan == "ru":
            switcher = {
                0: "Привет мой творческий программист!",
                1: "Пожалуйста выберите язык. Для английского скажи: 1 - Для русского скажи: 2",
                2: "Я что-то не понимаю, ты можешь повторить?",
                3: "Выбран русский язык! чем я могу тебе помочь?",
                4: "Слушаю...",
                5: "Открываю браузер, скажи адрес",
                6: "Прости! Я что-то не понимаю, ты можешь повторить?",
                7: "Текущее время ",
            }
        return switcher.get(id)
    except:
        return ""