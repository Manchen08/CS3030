#!/usr/bin/env python3
import sys
import sqlite3
import time
import datetime
import random

def create_table(cur):
    """
    Create a DB table
    Arg: cur => your DB cursor
    Returns: nothing
    """
    cur.execute("CREATE TABLE IF NOT EXISTS stuffToPlot (unix REAL, dateStamp TEXT, keyword TEXT, value REAL)")
    print("Created Table")

def create_date(cur):
    data = {}

    for item in range(10):
        data['unix'] = int(time.time())
        data['date'] = str(datetime.datetime.fromtimestamp(data['unix']).strftime('%Y-%m-%d %H:%M:%S'))
        data['keyword'] = "Python"
        data['value'] = random.randrange(0,10)
        # Insert record
        data_entry(cur, data)
        time.sleep(1)


def data_entry(cur, data):
    """
    Insert data to DB
    Arg: cur => your DB cursor
    Returns: nothing
    """
    # 1. Execute your INSERT
    cur.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES(?, ?, ?, ?)", (data['unix'], data['date'], data['keyword'], data['value']))
    print("Record inserted")

def read_db_data(cur):
    """
    Select Data from DB
    """
    cur.execute('SELECT * FROM stuffToPlot WHERE value=6.0')
    recs = cur.fetchall()

    for row in recs:
        print(row)

#Main function
def main():
    """
    Test Function
    """
    conn = sqlite3.connect('tutorial.db')
    if(conn):
        print("Connected to DB");

    # Need a cursor
    c = conn.cursor()
    # Create a table
    #create_table(c)


    # Insert data dynamically
    #create_data(c)
    
    read_db_data(c)
    # 2. Commit the change
    conn.commit()
    
    # Close Cursor
    c.close()
    # Close DB Connection
    conn.close()

if __name__ == "__main__":
    # Call Main
    main()

    exit(0)
