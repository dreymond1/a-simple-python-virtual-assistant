from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json

# Começo da sintese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)  # garante que sairá em portugues

# Função para receber a mensagem falada


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Fim da sintese de fala


# Começo do reconhecimento por voz
model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

while True:
    data = stream.read(8192)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']
            # printa o que foi dito
            print(text)
            # repete em voz o que foi dito
            speak(text)
