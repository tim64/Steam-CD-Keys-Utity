# -*- coding: utf-8 -*-
# !/usr/local/bin/python3
import sys
import os

txt_ext = ".txt"  # extension
space_char = " "
empty_char = ""
bad_spaces = "\xc2\xa0"  # non-breaking-space


# Функция перезаписывает файл и записывает в него все ключ, кроме тех, которые мы отсекли ранее
def delete_keys_from_original(key_count, key_list, filename):
    f = open(filename, "w")
    max_lines = len(key_list)
    for index, key in enumerate(key_list):
        if index == max_lines - key_count:
            f.close()
            return
        else:
            f.writelines(key)


# Функция записывает ключи в новый файл
def write_new_keys(key_count, key_list, filename):
    f = open(filename, "w")
    for index, key in enumerate(reversed(key_list)):
        if index == key_count:
            f.close()
            return
        else:
            f.writelines(key)


# Функция проверяет доступность файла для чтения
def check_file_read(filename):
    try:
        open(filename, 'rb')
    except IOError:
        print "Could not read file:", filename
        return False

    return True


# Функция получает список ключей из файла
def get_keys_from_file(filename):
    if check_file_read(filename):
        f = open(filename)
        keys = f.readlines()
        f.close()
        return keys


# Функция очищает строку от лишних символов и возвращает лист из слов в строке
def get_words_from_name(file_name):
    fix_name = file_name.replace(bad_spaces, space_char)  # удаляем non-breaking пробелы из строки
    fix_name = space_char.join(fix_name.split())  # удаляем лишние пробелы

    word_list = fix_name.split(space_char)  # собираем список из слов
    return word_list


# Функция заменяет количество ключей в имени файла на новое
def replace_key_count(file_name, key_count):
    file_name = file_name.replace(txt_ext, empty_char)

    word_list = file_name.split(space_char)
    for i in range(len(word_list)):
        if word_list[i].isdigit() and len(word_list[i]) > 1:
            word_list[i] = str(key_count)

    ready_name = space_char.join(word_list)
    return ready_name + txt_ext


# Функция переименовывает файл
def rename_original(old_name, new_name):
    os.rename(old_name, new_name)


def main(original_name, key_count):
    # Получение всех ключей из файла
    keys = get_keys_from_file(original_name)

    key_count = int(key_count)

    current_key_count = len(keys)

    new_name = replace_key_count(original_name, key_count)
    new_original_name = replace_key_count(original_name, current_key_count - key_count)

    # Записываем нужное кол-во ключей в новый файл
    write_new_keys(key_count, keys, new_name)

    # Удаляем соответствующие строки в исходном файле (перезаписываем файл заново)
    delete_keys_from_original(key_count, keys, original_name)
    rename_original(original_name, new_original_name)
    return


def test():
    main("/Users/user/Downloads/Longest Monday 4400 Free — копия.txt", 100)


#test()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
