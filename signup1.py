import mysql.connector;
con=mysql.connector.connect(host="localhost",user="root",password="root",database="test");
operation=con.cursor();
sql="insert into signin values('pooja', 'shreenu', 123, 'indore', 'indore', 'mp', 452001)";
operation.execute(sql);
con.commit();
con.close();
print("Record Inserted");