# Реализуйте класс Date, который должен:
#     проверять числа даты на корректность
#     конвертировать строку даты в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
#     Оба метода должны получать на вход строку вида ‘dd-mm-yyyy’.

# Пример основного кода:
#     date = Date.from_string('10-12-2077')
#     print(date)
#     print(Date.is_date_valid('10-12-2077'))
#     print(Date.is_date_valid('40-12-2077'))

# Результат:
#     День: 10    Месяц: 12    Год: 2077
#     True
#     False


class Date:
    @classmethod
    def from_string(cls, date: str) -> str:
        """
        Args:
            date (str): Дата в формате 'dd-mm-yyyy'

        Returns:
            str: Дата в формате 'День: ... Месяц: ... Год: ...'
        """
        day, month, year = map(int, date.split('-'))
        return f'День: {day}\tМесяц: {month}\tГод: {year}'

    @classmethod
    def is_date_valid(cls, date: str) -> bool:
        """
        Args:
            date (str): Дата в формате 'dd-mm-yyyy'

        Returns:
            bool: Дата является корректной
        """
        try:
            day, month, year = map(int, date.split('-'))
        except ValueError:
            return False

        if 0 < day < 32 and 0 < month < 13 and year >= 0:
            return True

        return False


print(Date.is_date_valid('31-11-2022'))
print(Date.is_date_valid('31-13-2022'))

print(Date.from_string('31-12-2022'))