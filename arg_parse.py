# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:22:01 2020

@author: kocha
"""
import argparse

parser = argparse.ArgumentParser(
    description="Parses input to identify schema and tables"
)

parser.add_argument("-s", "--schema", help="Schema name", required=True)
parser.add_argument("-t", "--tables", help="Table name(s)", required=False)
args = parser.parse_args()

tables = args.tables.split(",")

print(args.schema)
print(type(tables))
print(tables)
