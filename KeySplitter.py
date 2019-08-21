# coding=utf-8
# !/usr/local/bin/python3
import sys


def main(open_filename, key_count):
    f = open(open_filename)
    lines = f.readlines()
    all_keys_count = len(lines) - 1

    folder_path = open_filename[0:open_filename.rfind("/") + 1]

    index = 0
    new_name = folder_path + "New Keys " + str(key_count)

    new_f = open(new_name + ".txt", "w")

    for line in reversed(lines):
        new_f.writelines(line)
        index += 1
        if index >= key_count:
            break

    new_f.close()
    f.close()

    f = open(open_filename, "w")
    for i in range(all_keys_count):
        f.writelines(lines[i])
        if i >= (int(all_keys_count) - int(key_count)):
            f.close()
            return

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
