import mysql.connector
from mysql.connector import Error
import pandas as pd

def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="123"
    )

    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE testdb")

if __name__ == "__main__":
    main()