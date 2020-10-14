import csv
import random as rand
import string
from pathlib import Path
from random import choice


class create_test_data:
    def __init__(self, file_name, delim, column_count, row_count, val_len):
        self.home = str(Path.home())
        self.column_count = input("Enter number of columns to create: ")
        self.row_count = input("Enter number of rows to create: ")
        self.delim = input("Enter delimiter. If tab, enter 'tab': ")
        if self.delim == "tab":
            self.delim = "\t"
        self.val_len = input("Enter length for random string or integer: ")
        self.file_name = input("Enter file name: ")
        self.schema_name = input("Enter schema name for DDL: ")
        self.table_name = input("Enter table name for DDL: ")

    def rand_string(self):
        n = int(self.val_len)
        text = "".join(rand.choices(string.ascii_uppercase, k=n))
        return text

    def rand_integer(self):
        n = int(self.val_len)
        num = rand.randint(pow(10, n - 1), pow(10, n) - 1)
        return num

    def write_test_data(self):
        val_len = self.val_len
        csv_write_path = f"{self.home}/{self.file_name}.csv"
        column_count = int(self.column_count)
        header = ["C" + str(i + 1) for i in range(column_count)]
        value_list = [self.rand_string(val_len), self.rand_integer(val_len)]
        row = [choice(value_list) for i in range(column_count)]
        with open(csv_write_path, mode="w", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=self.delim)
            writer.writerow(header)
            for i in range(int(self.row_count)):
                writer.writerow(row)

    def write_stage_table_ddl(self):
        ddl_write_path = f"{self.home}/{self.table_name}.sql"
        column_count = int(self.column_count)
        header = ["C" + str(i + 1) for i in range(column_count)]
        row = self.row
        qual_table = f"{self.schema_name}.{self.table_name}"
        data_types = ["numeric" if str(i).isnumeric() else "text" for i in row]
        ddl_list = list(zip(header, data_types))
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
