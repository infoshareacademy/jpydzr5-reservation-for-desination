from datetime import datetime, timedelta
class Menu:
    def __init__(self):
        self.__option = '0'

    def __str__(self):
        message = ''
        match self.option:
            case '0':
                message += 'Witamy w naszym kinie! Wybierz jedną z opcji poniżej\n'
                message += ('1. Cennik\n'
                            '2. Repertuar\n'
                            '3. Wyświetl koszyk\n'
                            '4. Zakończ program\n')
            case '1':
                message += 'Wybrano cennik'
            case '2':
                now = datetime.today().weekday()
                end_date_week = (datetime.today() - timedelta(days=6 - now)).strftime("%Y-%m-%d")
                message += f'Repertuar na aktualny tydzień {datetime.today().strftime("%Y-%m-%d")} - {end_date_week}'
            case '3':
                message += 'Wybrano wyświetl koszyk'
            case _:
                message += 'Nie wybrano żadnej z dostępnych opcji!'
        return message

    @property
    def option(self) -> str:
        return self.__option

    @option.setter
    def option(self, value) -> None:
        self.__option = value
