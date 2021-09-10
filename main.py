import speech_recognition as sr

#Cria um reconhecedor
r = sr.Recognizer()

#Captura o audio do microfone
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) #Define o microfone para a saida de audio
        print(r.recognize_google(audio, language='pt')) #printa o que foi dito no microfone
        