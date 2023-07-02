import mysql.connector

from mysql.connector import Error


def getConecction():

    try:
    
        bd= mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='tutobqv2'
        )
        return bd
    except Error as e:
        print(e)


