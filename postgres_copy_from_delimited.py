import getpass
import os
import time
from datetime import timedelta

import psycopg2


def copy_from_local():
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
            cur.copy_expert(copy_sql, f, size=8192)


if __name__ == "__main__":

    print("\nThis application will load delimited files via postgres COPY\n")

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
        print("\nConnection Successful!\n")

    file_dir = input("Enter fully qualified file path source to copy from: ")
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

    cur = conn.cursor()

    print(f"\nCopying data from {file_dir} into {qual_table}...\n")

    copy_start_time = time.time()

    copy_from_local()

    copy_elapsed_time = time.time() - copy_start_time
    copy_elapsed_time = str(timedelta(seconds=copy_elapsed_time))

    conn.commit()
    cur.close()

    print(f"\nCopying completed in {copy_elapsed_time}\n")
