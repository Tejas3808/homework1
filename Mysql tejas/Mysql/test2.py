import mysql.connector as connection

mydb = connection.connect(host = "localhost" , user ="root" , passwd = "Root@123" )
cursor = mydb.cursor()
r = "create table ritika.details(id int(10)  , name varchar(80) , class varchar(20))"
cursor.execute(r)
mydb.commit()