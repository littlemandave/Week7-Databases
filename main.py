#!/usr/bin/env python3

"""
A little program to practice with databases
"""

import pyodbc
from contextlib import closing

def connectToDB():
    connection = pyodbc.connect(
        server="cisdbss.pcc.edu",
        database="IMDB",
        user="275student",
        password="275student",
        tds_version="7.4",
        port="1433",
        driver="FreeTDS"
    )

    if connection:
        print('Connected!')
        return connection
    else:
        print('Connection Failed.')
        return None

def GetRows(cursor, selectCmd):
  cursor.execute(selectCmd)
  return cursor.fetchall()

def GetOneRow(cursor, selectCmd):
  cursor.execute(selectCmd)
  return cursor.fetchone()

def PrintSelectedRows(cursor, selectCmd, msg = ''):
  rows = GetRows(cursor, selectCmd)
  print(msg)
  for r in rows:
    print(r)
  print()

def PrintOneRow(cursor, selectCmd, msg = ''):
  row = GetOneRow(cursor, selectCmd)
  print(msg)
  print(row)
  print()

def main():
    print()
    connection = connectToDB()
    if connection:
        with closing(connection.cursor()) as cursor:
            PrintSelectedRows(cursor, "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'", 'The whole thing:')
            # columns = cursor.execute("SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='name_basics'")
            # for column in columns:
            #     print(column)
            #PrintOneRow(cursor, "SELECT * FROM name_basics WHERE primaryName = 'Brad Pitt'")
            cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
            tables = cursor.fetchall()
            for table in tables:
                name = table[2]
                cmd = "SELECT COUNT(*) FROM " + name
                cursor.execute(cmd)
                aTuple = cursor.fetchone()
                print('Table ' + name + ' has ' + str(aTuple[0]) + ' rows.')

            # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
