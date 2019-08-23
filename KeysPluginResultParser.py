# coding=utf-8
# !/usr/local/bin/python3
import sys
import datetime
from time import gmtime, strftime


def check_key_activation(key):
    if key.find("Не активирован") != -1:
        return False
    else:
        return True


def main(open_filename):
    f = open(open_filename)
    frm = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    new_name = open_filename[open_filename.rfind("/") + 1:len(open_filename)].replace(".csv", "")
    folder_path = open_filename[0:open_filename.rfind("/") + 1]
    new_f = open(folder_path + new_name + " " + datetime.datetime.now().time().strftime(frm) + ".txt", "w")

    line = f.readline()

    while line:
        line = f.readline()
        activation = check_key_activation(line)
        if not activation:
            new_f.writelines(line.replace(',Не активирован', ''))
    f.close()
    new_f.close()


if __name__ == "__main__":
    main(sys.argv[1])
