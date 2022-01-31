import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="@Raja007", database='sql_store')

mycursor = mydb.cursor()

mycursor.execute('select * from customers')

# for i in mycursor:
# 	print(i)

result = mycursor.fetchone()

for i in result:
	print(i)

