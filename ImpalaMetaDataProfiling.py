import argparse
import csv
from pathlib import Path

import pyodbc


# Strips data defintion length, scale, etc. to build profiling queries
def format_data_type(data_type):
    formatted_data_type = ""
    for char in data_type:
        if char.isalpha():
            formatted_data_type += char
    return formatted_data_type


# Returns table row count
def getTableRowCount(schema_name, table_name, conn):
    row_count = f"SELECT count(*) from {schema_name}.{table_name};"
    query = conn.execute(row_count)
    rows = query.fetchone()
    return rows[0]


# Dynmaically builds profiling queries based on table column data types
def build_query(meta_data):
    freq_values_limit = 5
    schema_name = meta_data["schema_name"]
    column_name = meta_data["column_name"]
    data_type = meta_data["data_type"]
    table_name = meta_data["table_name"]
    row_count = meta_data["row_count"]
    data_type = meta_data["data_type"]
    mean_query = ""
    count_distinct_query = ""
    freq_values_query = ""
    null_query = ""
    min_query = ""
    max_query = ""

    if data_type not in [
        "char",
        "string",
        "timestamp",
        "varchar",
        "array",
        "map",
        "struct",
        "boolean",
    ]:  # if numeric
        mean_query = f"SELECT round(avg({column_name}), 2) \
                       FROM {schema_name}.{table_name};"
        null_query = f"select count(*) \
                       from {schema_name}.{table_name} \
                       where {column_name} is null;"
        min_query = f"SELECT MIN({column_name}) \
                      FROM {schema_name}.{table_name};"
        max_query = f"SELECT MAX({column_name}) \
                      FROM {schema_name}.{table_name};"
    elif data_type in ["char", "string", "varchar"]:  # if structured string
        count_distinct_query = f"select \
                              count(distinct nullif(trim({column_name}), '')) \
                              from {schema_name}.{table_name};"
        null_query = f"select count(*) \
                       from {schema_name}.{table_name} \
                       where nullif(trim({column_name}), '') is null;"
        freq_values_query = f"SELECT nullif(trim({column_name}), ''), \
                              count(*) \
                              FROM {schema_name}.{table_name} \
                              GROUP BY nullif(trim({column_name}), '') \
                              ORDER BY count(coalesce(nullif(trim \
                              ({column_name}), ''), '__NO_VALUE__' )) DESC \
                              LIMIT {freq_values_limit};"
    elif data_type == "timestamp":
        null_query = f"select count(*) \
                       from {schema_name}.{table_name} \
                       where {column_name} is null;"
        min_query = f"SELECT MIN({column_name}) \
                      FROM {schema_name}.{table_name};"
        max_query = f"SELECT MAX({column_name}) \
                      FROM {schema_name}.{table_name};"
    else:  # else, non-structured or BOOLEAN types
        null_query = f"select count(*) \
                       from {schema_name}.{table_name} \
                       where nullif(trim({column_name}), '') is null;"

    query_list = [
        schema_name,
        table_name,
        row_count,
        column_name,
        data_type,
        mean_query,
        count_distinct_query,
        freq_values_query,
        null_query,
        min_query,
        max_query,
    ]

    return query_list


# Executes profling queries and collects results for file output
def execute_query(query_list, conn):
    executed_queries = [query_list[i] for i in range(5)]
    for query in query_list[5:]:
        if query:
            query = conn.execute(query)
            rows = query.fetchall()
            if len(rows) == 1:
                rows = rows[0][0]
            else:  # return dictionary of value:count where NONE is replaced
                rows = [("NULL", i[1]) if i[0] is None else i for i in rows]
                rows = dict(rows)
            executed_queries.append(rows)
        else:
            executed_queries.append("")
    return executed_queries


# Writes profiling results to csv
def write_to_csv(query, writer):
    writer.writerow(query)


if __name__ == "__main__":

    # Create command line arguments
    parser = argparse.ArgumentParser(
        description="Parses input to identify schema and tables"
    )
    parser.add_argument("-s", "--schema", help="Schema name", required=True)
    parser.add_argument("-t", "--tables", help="Table name(s)", required=False)
    args = parser.parse_args()

    conn = pyodbc.connect("DSN=Impala", autocommit=True)  # Create connection

    schema = args.schema

    conn.execute(f"use {schema};")  # Use desired schema

    print(f"\nStarting metadata profiling in schema {schema}...\n")

    if args.tables:
        tables_list = args.tables.split(",")
    else:
        tables_crsr = conn.execute("show tables;")
        tables_list = [table[0] for table in tables_crsr.fetchall()]
        tables_crsr.close()

    mdata = []  # Initialize empty list to collect meta_data
    tables_dict = {}

    for table in tables_list:  # loop through table list to get table meta_data
        crsr = conn.execute(f"describe {table};")
        for row in crsr.fetchall():
            if table not in tables_dict.keys():
                tables_dict[table] = getTableRowCount(schema, table, conn)
            # append dicts of metatda for each table
            mdata.append(
                {
                    "schema_name": schema,
                    "table_name": table,
                    "column_name": row[0],
                    "data_type": format_data_type(row[1]),
                    "row_count": tables_dict[table],
                }
            )

    home = str(Path.home())  # get working directory path for writing results

    # Write profiling results to csv
    with open(
        f"{home}/profiling_results.csv", mode="w", newline="", encoding="utf-8"
    ) as data_file:
        data_writer = csv.writer(
            data_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        data_writer.writerow(
            [
                "Schema Name",
                "Table Name",
                "Total Row Count",
                "Column Name",
                "Data Type",
                "Average",
                "Distinct Count",
                "Most Frequent Values",
                "Null Count",
                "Min Value",
                "Max Value",
            ]
        )
        for query_data in mdata:
            query_table = query_data["table_name"]
            query_column = query_data["column_name"]
            print(f"Collecting metadata for {query_table}.{query_column}")
            query_list = build_query(query_data)
            query_rows = execute_query(query_list, conn)
            write_to_csv(query_rows, data_writer)

    crsr.close()
    conn.close()

    print(f"\nProfiling complete! Results at {home}\\profiling_results.csv\n")
