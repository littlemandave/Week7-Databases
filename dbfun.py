#!/usr/bin/env python3

"""
A little program to practice with databases
"""

import sqlite3
from contextlib import closing

def PrintSelectedPlanets(cursor, selectCmd, msg = ''):
  rows = GetRows(cursor, selectCmd)
  print(msg)
  for r in rows:
    print(r)
  print()

def GetRows(cursor, selectCmd):
  cursor.execute(selectCmd)
  return cursor.fetchall()

def main():
    #Connect to a SQLite Database....with SQL Server and pyodbc we would need login info and server name
    myConnection = sqlite3.connect("PlanetsDB")

    #get a cursor so we can send commands to the server
    # myCursor = myConnection.cursor()
    with closing(myConnection.cursor()) as myCursor:

      # kill any previous attempts at making the Planets table
      myCursor.execute("DROP TABLE IF EXISTS Planets")

      #create a table to put some data in (If it doesnt already exist)
      myCursor.execute("CREATE TABLE IF NOT EXISTS Planets(ID INTEGER PRIMARY KEY AUTOINCREMENT, Position INTEGER,Name STRING, Color STRING, Diameter REAL, OrbitRadius REAL, OrbitYears REAL);")

      #Insert Some Data
      myCursor.execute("INSERT INTO Planets(Position,Name,Color,Diameter,OrbitRadius,OrbitYears) values(1,'Mercury','Charcoal',0.38,0.39,0.24)")
      myCursor.execute("INSERT INTO Planets(Position,Name,Color,Diameter,OrbitRadius,OrbitYears) values(2,'Venus','Greenish',0.95,0.72,0.62)")
      myCursor.execute("INSERT INTO Planets(Position,Name,Color,Diameter,OrbitRadius,OrbitYears) values(3,'Earth','Blue',1.0,1.0,1.0)")
      myCursor.execute("INSERT INTO Planets(Position,Name,Color,Diameter,OrbitRadius,OrbitYears) values(4,'Mars','Red',0.53,1.52,1.88)")
      myCursor.execute("INSERT INTO Planets(Position,Name,Color,Diameter,OrbitRadius,OrbitYears) values(5,'Jupiter','Swirly',11.2,5.2,11.9)")
      myCursor.execute("INSERT INTO Planets(Position,Name,Color,Diameter,OrbitRadius,OrbitYears) values(6,'Saturn','Ringed',9.45,9.54,29.5)")

      #show it
      PrintSelectedPlanets(myCursor, "SELECT * FROM Planets ORDER BY Position", 'The whole thing:')

      # Just show the name and color of the outer PrintSelectedPlanets
      PrintSelectedPlanets(myCursor, 'SELECT Name, Color FROM Planets WHERE OrbitYears > 1.0 ORDER BY Name', 'Here are the outer planets:')

      print('Inserting new planet Tanglepuss')
      cmd = "INSERT INTO Planets(Position,Name,Color,Diameter,OrbitRadius,OrbitYears) values(0,'Tanglepuss','Purplish',0.18,0.21,0.1)"
      myCursor.execute(cmd)
      myConnection.commit()
      PrintSelectedPlanets(myCursor, "SELECT * FROM Planets ORDER BY Position", 'All planets now:')

      print('Modifying Tanglepuss')
      cmd = "UPDATE Planets SET OrbitYears = 2.3 WHERE Name = 'Tanglepuss'"
      myCursor.execute(cmd)
      myConnection.commit()
      PrintSelectedPlanets(myCursor, "SELECT * FROM Planets ORDER BY Position", 'Modified:')

      print('Deleting Tanglepuss')
      cmd = "DELETE FROM Planets WHERE Name = 'Tanglepuss'"
      myCursor.execute(cmd)
      myConnection.commit()
      PrintSelectedPlanets(myCursor, "SELECT * FROM Planets ORDER BY Position", 'No more Tanglepuss:')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()