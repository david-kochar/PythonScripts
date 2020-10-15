import getpass
import os
import time
from datetime import timedelta

import psycopg2


class copy_from_delimited:
    def postgres_connection(self):
        while True:
            try:
                db_username = input("Enter Username: ")
                db_password = getpass.getpass("Enter Password: ")
                db_name = input("Enter Database Name: ")
                db_host = input("Enter Host Name/Address: ")
                db_port = input("Enter Port: ")

                conn = psycopg2.connect(
                    user=db_username,
                    password=db_password,
                    host=db_host,
                    port=db_port,
                    database=db_name,
                )

                if conn:
                    print("\nConnection successful!\n")
                    conn.autocommit = True
                    crsr = conn.cursor()
                    return crsr
                    break
            except Exception:
                print("\nConnection failed. Please re-enter parameters.\n")

    def copy_from_local(self, crsr):
        copy_crsr = crsr
        file_dir = input("Enter full file directory to copy from: ")
        header = input("Do files have a header? (y/n): ")
        delim = input("Enter files' delimiter. If tab, enter 'tab': ")
        quote_char = input("Enter quote character: ")
        esc_char = input("Enter quote escape character: ")
        schema_name = input("Enter target schema name: ")
        table_name = input("Enter target table name: ")
        qual_table = f"{schema_name}.{table_name}"
        copy_list = [
            os.path.join(file_dir, f)
            for f in os.listdir(file_dir)
            if f[-3:] in ["txt", "csv"]
        ]

        if header.upper() == "Y":
            header = "HEADER"
        else:
            header = ""

        if quote_char == '"':
            quote_char = """'"'"""
        else:
            quote_char = "''''"

        if esc_char == '"':
            esc_char = """'"'"""
        else:
            esc_char = "''''"

        if delim == "tab":
            delim = "\t"

        print(f"\nCopying data from {file_dir} into {qual_table}...\n")

        copy_start_time = time.time()

        for file_path in copy_list:
            file_format = file_path[-3:]
            copy_sql = (
                f"COPY {qual_table} "
                f"FROM '{file_path}' "
                f"DELIMITER '{delim}' "
                f"{file_format} "
                f"{header} "
                f"QUOTE {quote_char} "
                f"ESCAPE {esc_char};"
            )
            print(f"Copying from {file_path}")
            with open(file_path, "r") as f:
                copy_crsr.copy_expert(copy_sql, f, size=8192)

        copy_elapsed_time = time.time() - copy_start_time
        copy_elapsed_time = str(timedelta(seconds=copy_elapsed_time))

        copy_crsr.close()

        print(f"\nCopying completed in {copy_elapsed_time}\n")
