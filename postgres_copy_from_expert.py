import getpass

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

    schema_name = input("Enter schema name: ")
    table_name = input("Enter table name: ")
    qual_table = f"{schema_name}.{table_name}"
    header = input("Does the file have a header? (y/n): ")
    delim = input("Enter delimiter. If tab, enter 'tab': ")
    file_format = input("Enter 'TEXT' or 'CSV' file format: ")
    file_path = input("Enter fully qualified file path: ")
    quote_char = input("Enter quote character: ")
    esc_char = input("Enter quote escape character: ")

    if quote_char == '"':
        quote_char = """'\\"'"""
    else:
        quote_char = "''''"

    if esc_char == '"':
        esc_char = """'\\"'"""
    else:
        esc_char = "''''"

    if delim == "tab":
        delim = "\t"

    copy_sql = f"COPY {qual_table} \
                 FROM '{file_path}' \
                 DELIMITER '{delim}' \
                 {file_format} \
                 QUOTE {quote_char} \
                 ESCAPE {esc_char};"

    cur = conn.cursor()

    print(f"\nCopying data into {schema_name}.{table_name}...\n")

    with open(file_path, "r") as f:
        if header.upper() == "Y":
            next(f)  # Skip the header row
            cur.copy_expert(copy_sql, f, size=8192)
        else:
            cur.copy_expert(copy_sql, f, size=8192)

    print("Copying data complete!\n")

    conn.commit()
    cur.close()


if __name__ == "__main__":
    copy_from_local()
