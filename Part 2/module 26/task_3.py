# Реализуйте функцию-генератор, которая берёт все питоновские файлы в директории и вычисляет
# количество строк в каждом файле, игнорируя пустые строки и строки комментариев.
# По итогу функция-генератор должна с помощью yield каждый раз возвращать количество строк в очередном файле.

import os


def gen_python_files(directory='C:/'):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                    non_empty_lines = [line for line in lines if line.strip() and not line.strip().startswith('#')]
                    yield file_path, len(non_empty_lines)