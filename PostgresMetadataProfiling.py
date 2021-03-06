import getpass  # for hiding password input

import pyodbc

# Build database connection string from input
dbDriver = input("Enter Database Driver: ")
dbType = input("Enter Database Type: ")
dbUID = input("Enter UID: ")
dbPassword = getpass.getpass("Enter Password: ")
dbServer = input("Enter Server Name: ")
dbPort = input("Enter Port: ")

# Format connection string
conn_str = (
    f"DRIVER={{{dbDriver}}};"
    f"DATABASE={dbType};"
    f"UID={dbUID};"
    f"PWD={dbPassword};"
    f"SERVER={dbServer};"
    f"PORT={dbPort};"
)

# Create connection
conn = pyodbc.connect(conn_str)

# Results are based on user supplied schema(s) and table(s)
schemas = input("Enter schema(s) for profiling separated by commas: ")
tables = input("Enter table(s) for profiling separated by commas: ")

"""
#format input to pass as SQL parameters to ODBC
schemas = ','.join("'{}'".format(word.strip()) for word in schemas.split(','))
tables = ','.join("'{}'".format(word.strip()) for word in tables.split(','))
"""

# Example querying of postgres metadata
crsr = conn.execute(
    """
                     select table_schema,
                       table_name,
                       column_name,
                       data_type
                     from information_schema.columns
                     where table_schema in (?)
                     and table_name     in (?)
                     """,
    schemas,
    tables,
)

rows = crsr.fetchmany()

# Initialize empty list to collect metadata
mdata = []

# Append dicts of metadata
for row in crsr.fetchall():
    mdata.append(
        {
            "schema": row[0],
            "table_name": row[1],
            "column_name": row[2],
            "data_type": row[3],
        }
    )

print(mdata)

crsr.close()
conn.close()
