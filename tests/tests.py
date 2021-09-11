import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id) #garante que sairá em portugues
engine.say("Eu vou falar este texto")
engine.runAndWait()