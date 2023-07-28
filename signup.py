#pip  insall pymysql

import mysql.connector;
email=input("enter your email id");
name=input("Enter your Name");
pwd=input("Enter password");
address=input("enter your address");
city=input("enter your city");
state=input("enter your state");
pincode=input("enter your pincode");
con=mysql.connector.connect(host="localhost",user="root",password="root",database="test")
operation=con.cursor();
sql="insert into signin values(%s,%s,%s,%s,%s,%s,%s)";
values=(email,name,pwd,address,city,state,pincode);
operation.execute(sql,values);
con.commit();
con.close();
print("Record Inserted");