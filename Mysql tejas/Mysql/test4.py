import mysql.connector as connection

mydb = connection.connect(host = "localhost" , user ="root" , passwd = "Root@123" )
cursor = mydb.cursor()
cursor.execute("select * from ritika.details")
for r in cursor.fetchall():
    print( r)