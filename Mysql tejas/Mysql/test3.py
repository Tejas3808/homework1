import mysql.connector as conn

mydb = conn.connect(host = "localhost" , user ="root" , passwd = "Root@123" )
cursor = mydb.cursor()
s = "insert into ritika.details values(101,'Ritika','Mca')"
cursor.execute(s)
mydb.commit()