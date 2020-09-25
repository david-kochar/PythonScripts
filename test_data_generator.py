import csv
import random as rand
import string
from pathlib import Path
from random import choice


def rand_string():
    text = "".join(rand.choices(string.ascii_uppercase + string.digits, k=20))
    return text


def rand_integer():
    return rand.randint(1000000, 99999999)


home = str(Path.home())
header_count = input("\nEnter number of columns to create: ")
rows = input("Enter number of rows to create: ")
delim = input("Enter delimiter. If tab, enter 'tab': ")
file_name = input("Enter file name: ")
write_path = f"{home}/{file_name}.csv"

if delim == "tab":
    delim = "\t"

print("\nWriting test data delimited file...\n")

with open(write_path, mode="w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f, delimiter=delim)
    header = ["c" + str(i + 1) for i in range(int(header_count))]
    writer.writerow(header)
    for i in range(int(rows)):
        value_list = [rand_string(), rand_integer()]
        row = [choice(value_list) for i in range(int(header_count))]
        writer.writerow(row)

print(f"Test data writing completed at {home}\\{file_name}.csv\n")
