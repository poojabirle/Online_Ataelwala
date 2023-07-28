import mysql.connector;
email=input("enter your email id");
con=mysql.connector.connect(host="localhost",user="root",password="root",database="test");
operation=con.cursor();
#sql="select * from invoice;
sql="select * from invoice where email=%s";
values=(email);
operation.execute(sql,values);
records=operation.fetchall();
for data in records:
	print(data)
con.commit();
con.close();
print("Record Inserted");