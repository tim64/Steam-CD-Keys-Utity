# coding=utf-8
# !/usr/local/bin/python3
import sys


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


def main(original_filename, key_count):
    key_count = int(key_count)
    # Получение всех ключей из файла
    lines = get_file_strings(original_filename)

    # Создание пустого файла для новых ключей
    folder_path = original_filename[0:original_filename.rfind("/") + 1]
    new_filename = folder_path + "New Keys " + str(key_count)
    new_file = open(new_filename + ".txt", "w")

    # Записываем нужное кол-во ключей в новый файл
    write_new_keys(key_count, lines, new_file)

    # Удаляем соответствующие строки в исходном файле (перезаписываем файл заново)
    delete_keys_from_original(key_count, lines, original_filename)
    return


def test():
    main("/Users/user/Downloads/TestKeys1400.txt", 50)


#test()


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
