import mysql.connector

database = mysql.connector.connect(

    host = 'localhost',
    user = 'root',
    passwd = 'Vishal@1998'
)

cursorObject = database.cursor()


cursorObject.execute("CREATE DATABASE employee")

print("All Done")