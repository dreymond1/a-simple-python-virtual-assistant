import datetime
import os
import subprocess



class SystemInfo:
    def __init__(self):
        pass

    def get_time():
        now = datetime.datetime.now()
        answer = 'São {} horas e {} minutos'.format(now.hour, now.minute)
        return answer

    def get_date():
        now = datetime.datetime.now()
        answer = 'Hoje é dia {} do mês {} do ano de {}'.format(
            now.day, now.month, now.year)
        return answer

    def get_Notepad():
        answer = os.system('notepad.exe')
        return answer

    def get_Prompt():
        answer = os.system('cmd.exe')
        return answer

    def get_Chrome():
        answer = os.system('"C:/Program Files/Google/Chrome/Application/chrome.exe"')
        return answer
        
