# Напишите программу, которая считывает строки из файла и выводит строки, содержащие слово ERROR, в новый файл.

import random


def create_input_log(file_path, num_lines):
    errors = ['ERROR', 'CRITICAL', 'WARNING']
    with open(file_path, 'w') as file:
        for _ in range(num_lines):
            line = f"{random.choice(errors)}: This is a sample error message\n"
            file.write(line)


def error_log_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if 'ERROR' in line:
                yield line


def main():
    create_input_log('input.log', 1000)
    input_file = 'input.log'
    output_file = 'output.log'

    with open(output_file, 'w') as out_file:
        for error_line in error_log_generator(input_file):
            out_file.write(error_line)


main()
