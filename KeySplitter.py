# -*- coding: utf-8 -*-
# !/usr/local/bin/python3
import sys
import os


def delete_keys_from_original(key_count, lines, current_file):
    index = 0
    open_file = open(current_file, "w")
    max_lines = len(lines)
    for line in lines:
        open_file.writelines(line)
        index += 1
        if index >= max_lines - key_count:
            open_file.close()
            return


def write_new_keys(key_count, lines, current_file):
    index = 0

    for line in reversed(lines):
        current_file.writelines(line)
        index += 1
        if index >= key_count:
            current_file.close()
            return


def get_file_strings(open_filename):
    open_file = open(open_filename)
    lines = open_file.readlines()
    open_file.close()
    return lines


def get_count_from_filename(file_name):
    sep = " "

    fix_name = file_name.replace("—", sep).replace("\xc2\xa0", sep).replace(".txt", "")
    fix_name = sep.join(fix_name.split())

    word_list = fix_name.split(sep)

    for word in word_list:
        if word.isdigit() and len(word) > 1:
            return int(word)


def replace_key_count(file_name, count):
    file_name = file_name.replace(".txt", "")
    sep = " "

    word_list = file_name.split(sep)
    print (word_list)
    for i in range(len(word_list)):
        if word_list[i].isdigit() and len(word_list[i]) > 1:
            word_list[i] = str(count)

    ready_name = sep.join(word_list)
    return ready_name + ".txt"


def rename_original(old, new):
    os.rename(old, new)


def main(original_filename, key_count):
    key_count = int(key_count)
    # Получение всех ключей из файла
    lines = get_file_strings(original_filename)

    current_key_count = int(get_count_from_filename(original_filename))
    new_filename = replace_key_count(original_filename, key_count)
    new_original_filename = replace_key_count(original_filename, current_key_count - key_count)

    # Записываем нужное кол-во ключей в новый файл
    new_file = open(new_filename, "w")
    write_new_keys(key_count, lines, new_file)

    # Удаляем соответствующие строки в исходном файле (перезаписываем файл заново)
    delete_keys_from_original(key_count, lines, original_filename)
    rename_original(original_filename, new_original_filename)
    return


def test():
    main("/Users/user/Downloads/Rules of The Mafia Free 1690.txt", 100)


#test()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
