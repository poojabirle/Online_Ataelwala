import mysql.connector;
email=input("enter your email id");
servicename=input("Enter your serviceName");
timeslot=input("enter timeslot");
day=input("enter day for pickup");
contact=input("enter your contact");
pickuplocation=input("enter pickuplocation");
quantity=input("enter quantity in kilos");
con=mysql.connector.connect(host="localhost",user="root",password="root",database="test");
operation=con.cursor();
sql="insert into services values(%s,%s,%s,%s,%s,%s,%s)";
values=(email,servicename,timeslot,day,contact,pickuplocation,quantity);
operation.execute(sql,values);
con.commit();
con.close();
print("Record Inserted");