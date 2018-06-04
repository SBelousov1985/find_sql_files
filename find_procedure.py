# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))


def get_files(files, ext, filter_string):
    result = []
    path = os.path.join(current_dir, migrations)
    for file_name in files:
        if file_name.endswith("." + ext):
            with open(os.path.join(path, file_name)) as f:
                text = f.read()
                if filter_string.lower() in text.lower():
                    result.append(file_name)
    return result


def print_result(files):
    for file_name in files:
        print(os.path.join(migrations, file_name))
    print("Всего:", len(files))


if __name__ == '__main__':
    print(current_dir)
    path = os.path.join(current_dir, migrations)
    file_list = os.listdir(path)
    while True:
        filter_string = input("Введите строку: ")
        file_list = get_files(file_list, "sql", filter_string)
        print_result(file_list)
