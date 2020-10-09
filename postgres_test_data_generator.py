import csv
import random as rand
import string
import time
from pathlib import Path
from random import choice


def rand_string(n):
    n = int(n)
    text = "".join(rand.choices(string.ascii_uppercase, k=n))
    return text


def rand_integer(n):
    n = int(n)
    num = rand.randint(pow(10, n - 1), pow(10, n) - 1)
    return num


def write_test_data():
    with open(csv_write_path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=delim)
        writer.writerow(header)
        for i in range(int(rows)):
            writer.writerow(row)


def create_ddl():
    with open(ddl_write_path, mode="w") as f:
        f.write(f"DROP TABLE IF EXISTS {qual_table};\n")
        f.write(f"CREATE UNLOGGED TABLE {qual_table} (\n")
        for i in range(len(ddl_list) - 1):
            col = ddl_list[i][0]
            data_type = ddl_list[i][1]
            f.write(f"{col} {data_type},\n")
        last_col = ddl_list[-1][0]
        last_data_type = ddl_list[-1][1]
        f.write(f"{last_col} {last_data_type}")
        f.write(" );")


if __name__ == "__main__":

    intro = """
This application will create test data with random strings and integers of
specified length, and will also generate corresponding DDL. Columns are
generically named C1, C2...Cn. Test data will be written in csv format to the
current working directory.
    """

    print(intro)

    time.sleep(3)

    home = str(Path.home())
    column_count = input("Enter number of columns to create: ")
    rows = input("Enter number of rows to create: ")
    val_len = input("Enter length for random string or integer: ")
    delim = input("Enter delimiter. If tab, enter 'tab': ")
    file_name = input("Enter file name: ")
    csv_write_path = f"{home}/{file_name}.csv"
    schema_name = input("Enter schema name for DDL: ")
    table_name = input("Enter table name for DDL: ")
    ddl_write_path = f"{home}/{table_name}.sql"
    qual_table = f"{schema_name}.{table_name}"
    header = ["C" + str(i + 1) for i in range(int(column_count))]
    value_list = [rand_string(val_len), rand_integer(val_len)]
    row = [choice(value_list) for i in range(int(column_count))]
    data_types = ["numeric" if str(i).isnumeric() else "text" for i in row]
    ddl_list = list(zip(header, data_types))

    if delim == "tab":
        delim = "\t"

    print("\nGenerating test data...\n")

    write_test_data()
    create_ddl()

    print(f"Test data generated to {home}\\{file_name}.csv\n")

    print(f"Test data DDL generated to {home}\\{table_name}.sql\n")
