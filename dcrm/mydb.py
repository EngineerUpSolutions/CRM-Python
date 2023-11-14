import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '123456WaW'

)


cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE clients")

print("ALL DONE!")