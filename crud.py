import mysql.connector as connector  #importing mysql.connector driver

class DBHelper:
  con = connector.connect(host='localhost',
                          port=3306,
                          user='root',
                          password='Idiot@123', 
                          database='college') #Establicshing the connection
  cursor = con.cursor(); #creating cursor object
  
  #creating the table if not exists using constructor
  def __init__(self,):
    query= '''CREATE TABLE IF NOT EXISTS STUDENT(NAME VARCHAR(10), SID VARCHAR(10), AGE INT(3), COURSE VARCHAR(10))'''
    self.cursor.execute(query)
    self.con.commit()
    print("")
    print("Table created successfully")
    print("")
  
  #inserting the values into table
  def insert(self,name,sid,age,course):
    query= '''INSERT INTO STUDENT VALUES('{}','{}',{},'{}')'''.format(name,sid,age,course)
    self.cursor.execute(query)
    self.con.commit()
    print("")
    print('Inserted succcessfully')
    print("")
  
  #diplaying the table
  def showdatabase(self):
    query='''SELECT * FROM STUDENT'''
    self.cursor.execute(query)
    print("")
    print("Showing the table.....")
    print("")
    print(self.cursor.fetchall())
    print("")
  
  #updating the values in the table  
  def update(self,name,sid):
    query= '''UPDATE STUDENT SET NAME='{}' WHERE SID='{}' '''.format(name,sid)
    self.cursor.execute(query)
    self.con.commit()
    print('Name updated successfully')
    print("")
  
  #deleting the entire table if exits
  def drop(self):
    query= 'DROP TABLE IF EXISTS STUDENT'
    self.cursor.execute(query)
    self.con.commit()
    print("")
    print("Table Dropped successfully")
    print("")
    
  #deleting the data in the table
  def delete(self,sid):
    query= '''DELETE FROM STUDENT WHERE SID='{}' '''.format(sid)
    self.cursor.execute(query)
    self.con.commit()
    print("")
    print("Row deleted successfully")
    print("")
  
  #dipslying the data using clauses
  def clause(self):
    query='SELECT * FROM STUDENT ORDER BY AGE'
    print("")
    print('Displaying the data using order by clause')
    self.cursor.execute(query)
    print(self.cursor.fetchall())
    
    query='SELECT * FROM STUDENT LIMIT 2'
    print()
    print('Displaying the data using limit clause')
    self.cursor.execute(query)
    print(self.cursor.fetchall())
    print("")
