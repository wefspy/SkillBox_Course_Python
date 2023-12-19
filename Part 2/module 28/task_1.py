# Реализуйте модернизированную версию контекст-менеджера File:

# теперь при попытке открыть несуществующий файл менеджер должен автоматически создавать и открывать этот файл в режиме записи;
# на выходе из менеджера должны подавляться все исключения, связанные с файлами.

from typing import TextIO


class File:
    """
        Контент менеджер, открывающий файл в режиме записи в случае FileNotFoundError
    """

    def __init__(self, file_name, mode) -> None:
        self.file_name = file_name
        self.mode = mode
        self.file = None

    def __enter__(self) -> 'TextIO':
        try:
            self.file = open(self.file_name, self.mode, encoding='UTF-8')
        except FileNotFoundError:
            self.file = open(self.file_name, 'w', encoding='UTF-8')

        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file is not None:
            self.file.close()
        return True


with File('test.txt', 'r') as test:
    print(test)
