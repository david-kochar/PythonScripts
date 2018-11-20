# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 10:57:34 2018

@author: DK

Using the same SQLite installation, perform the following tasks. Write your code in a Python
file and run it.

1) create a database called inventory
2) create a table called fruits with the following fields: name varchar(100), quantity
   integer, cost double
3) insert the following records into the fruit table:
a) “apple”, 20, 1.01
b) “oranges”, 100, 2.01
c) “bananas”, 0, 1.50
4) update the fruit table so that there are 0 apples
5) delete from the fruit table all fruits that are not in our inventory (quantity equals 0)
6) save your changes and close the connection
    
"""
#Pre-requisite for Windows machine: installed sqlite-tools from
#https://www.sqlite.org/2018/sqlite-tools-win32-x86-3250300.zip

import sqlite3

sqlite_db = 'inventory.sqlite'
conn = sqlite3.connect(sqlite_db)
inventory_connect = conn.cursor()

# Execute DDL
inventory_connect.execute(
        'CREATE TABLE {table_name} ({name} {name_def}, {quantity} \
        {quantity_def}, {cost} {cost_def})'.format(table_name="fruits",
        name = "name", name_def = "varchar(100)",
        quantity ="quantity", quantity_def="integer",
        cost = "cost", cost_def = "double" )
        )

#Insert fruits        
inventory_connect.execute(
        'INSERT INTO {table_name} ({name}, {quantity}, {cost}) \
        VALUES ("apple", 20, 1.01 )'.format(table_name="fruits",
        name = "name",
        quantity ="quantity",
        cost = "cost")
        )

inventory_connect.execute(
        'INSERT INTO {table_name} ({name}, {quantity}, {cost}) \
        VALUES ("oranges", 100, 2.01 )'.format(table_name="fruits",
        name = "name",
        quantity ="quantity",
        cost = "cost")
        )
        
inventory_connect.execute(
        'INSERT INTO {table_name} ({name}, {quantity}, {cost}) \
        VALUES ("bananas", 0, 1.5 )'.format(table_name="fruits",
        name = "name",
        quantity ="quantity",
        cost = "cost")
        )

#Update apple quantity
inventory_connect.execute(
        'UPDATE {table_name} SET {quantity} = 0 \
        WHERE name = "apple"'.format(table_name="fruits",
        name = "name",
        quantity = "quantity")
        )

#Delete records where quantity is zero        
inventory_connect.execute(
        'DELETE FROM {table_name} WHERE {quantity} = 0'.\
        format(table_name="fruits", quantity = "quantity")
        )

conn.commit()
conn.close()    