import datetime


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
