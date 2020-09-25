import argparse
import getpass  # for hiding password input

import pyodbc

parser = argparse.ArgumentParser(
    description="Parses input to identify schema and tables"
)

parser.add_argument("-s", "--schema", help="Schema name", required=True)
parser.add_argument("-t", "--tables", help="Table name(s)", required=False)
args = parser.parse_args()

# Build database connection string from input
dbUID = input("Enter Username: ")
dbPassword = getpass.getpass("Enter Password: ")

# Format connection string
conn_str = (
    "DRIVER={PostgreSQL ANSI(x64)};"
    "DATABASE=postgres;"
    f"UID={dbUID};"
    f"PWD={dbPassword};"
    f"SERVER=localhost;"
    f"PORT=5432;"
)

# Create connection
conn = pyodbc.connect(conn_str)

schema = args.schema

base_sql = (
    "select table_schema, table_name, column_name, data_type "
    "from information_schema.columns "
    "where table_schema = ?"
)

if args.tables:  # if tables were passed as arg, add tables to predicate
    tables = tuple(
        args.tables.split(",")
    )  # convert tables arg into tuple to pass as sql param
    placeholders = ",".join(
        "?" * len(tables)
    )  # make parameter placeholders for each table name in tables arg
    sql = (
        base_sql + " and table_name in (%s)" % placeholders
    )  # build query with placeholders
    params = [schema]  # add schema to params list
    params.extend(tables)  # extend params list with table names
    crsr = conn.execute(sql, params)  # execute sql with params
else:  # if no tables were passed as arg, select all tables
    crsr = conn.execute(base_sql, schema)

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
