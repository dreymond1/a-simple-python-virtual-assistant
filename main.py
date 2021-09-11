from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import core

# Começo da sintese de fala
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[-2].id)  # garante que sairá em portugues

# Função para receber a mensagem falada


def speak(text):
    engine.say(text)
    engine.runAndWait()

# Fim da sintese de fala


# Reconhecimento de fala
model = Model("model")
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=2048)
stream.start_stream()

# Loop do reconhecimento de fala
while True:
    data = stream.read(2048)
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
            # speak(text)

            if text == 'que dia é hoje':
                speak(core.SystemInfo.get_date())

            if text == 'que horas são':
                speak(core.SystemInfo.get_time())
