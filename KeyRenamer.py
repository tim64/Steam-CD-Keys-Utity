# -*- coding: utf-8 -*-
# !/usr/local/bin/python3

"""
Скрипт для быстрого переименования файла с ключами
Алгоритм работы:
1) Берем файл с ключами
2) Считаем количество ключей внутри
3) Запрашиваем у пользователя, что это за игра и какой партнер
4) Переименовываем
"""

import sys
import os

space_char = " "
txt_ext = ".txt"


# Функция получает список ключей из файла
def get_keys_from_file(filename):
    if check_file_read(filename):
        f = open(filename)
        keys = f.readlines()
        f.close()
        return keys


# Функция проверяет доступность файла для чтения
def check_file_read(filename):
    try:
        open(filename, 'rb')
    except IOError:
        print "Не могу прочитать файл:", filename
        return False
    except SystemError:
        print "С файлом что-то не так:", filename
        return False

    return True


def main(original_filename, game_name, partner_name):
    keys = get_keys_from_file(original_filename)
    # считаем количество ключей
    key_count = str(len(keys))
    # берем путь до папки
    folder_path = original_filename[0:original_filename.rfind("/") + 1]
    # переименовываем по нужному формату
    new_name = folder_path + game_name + space_char + key_count + space_char + partner_name + txt_ext
    # переименовываем в системе
    os.rename(original_filename, new_name)


def test():
    main("/Users/user/Downloads/test.csv", "GameTest", "Groupees")


#test()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
