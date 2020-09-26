import csv
import random as rand
import string
import time
from pathlib import Path
from random import choice


def rand_string(n):
    n = int(n)
    text = "".join(rand.choices(string.ascii_uppercase + string.digits, k=n))
    return text


def rand_integer(n):
    n = int(n)
    num = rand.randint(pow(10, n - 1), pow(10, n) - 1)
    return num


def write_test_data():
    with open(write_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=delim)
        header = ["C" + str(i + 1) for i in range(int(header_count))]
        writer.writerow(header)
        for i in range(int(rows)):
            value_list = [rand_string(val_len), rand_integer(val_len)]
            row = [choice(value_list) for i in range(int(header_count))]
            writer.writerow(row)


if __name__ == "__main__":

    intro = """
This application will create test data with random strings and integers of
specified length. Columns are generically named C1, C2...Cn. Test data will
be written in csv format to the current working directory.
    """

    print(intro)

    time.sleep(3)

    home = str(Path.home())
    header_count = input("Enter number of columns to create: ")
    rows = input("Enter number of rows to create: ")
    val_len = input("Enter length for random string or integer: ")
    delim = input("Enter delimiter. If tab, enter 'tab': ")
    file_name = input("Enter file name: ")
    write_path = f"{home}/{file_name}.csv"

    if delim == "tab":
        delim = "\t"

    print("\nWriting test data delimited file...\n")

    write_test_data()

    print(f"Test data writing completed at {home}\\{file_name}.csv\n")
