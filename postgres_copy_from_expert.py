import getpass
import os

import psycopg2


def copy_from_local():
    db_username = input("\nEnter Username: ")
    db_password = getpass.getpass("Enter Password: ")
    db_name = input("Enter Database Name: ")
    db_host = input("Enter Server Host: ")
    db_port = input("Enter Port Number: ")

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

    copy_list = [
        os.path.join(file_dir, f)
        for f in os.listdir(file_dir)
        if f[-3:] in ["txt", "csv"]
    ]

    for file_path in copy_list:
        file_format = file_path[-3:]
        copy_sql = (
            f"COPY {qual_table} "
            f"FROM '{file_path}' "
            f"DELIMITER '{delim}' "
            f"{file_format} "
            f"QUOTE {quote_char} "
            f"ESCAPE {esc_char};"
        )
        print(f"Copying from {file_path}")
        with open(file_path, "r") as f:
            if header.upper() == "Y":
                next(f)  # Skip the header row
                cur.copy_expert(copy_sql, f, size=8192)
            else:
                cur.copy_expert(copy_sql, f, size=8192)

    conn.commit()
    cur.close()

    print("\nCopying data complete!\n")


if __name__ == "__main__":
    copy_from_local()
