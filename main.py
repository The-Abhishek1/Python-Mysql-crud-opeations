from crud import DBHelper 

def main():
  while True:
    print("****WELCOME****")
    print("")
    print("Press 1 to create a tabel..")
    print("Press 2 to Insert the values..")
    print("Press 3 to Display the table..")
    print("Press 4 to Update the values..")
    print("Press 5 to Drop the table..")
    print("Press 6 to Delete the values..")
    print("Press 7 to Display the data using clauses..")
    print("Press 8 to Exist..")
    choice=int(input("Enter your choice: "))
    try:
      if choice==1:
        db=DBHelper()
      elif choice==2:
        name=input("Enter the Name: ")
        sid=input("Enter the SID: ")
        age=int(input("Enter the Age: "))
        course=input("Enter the course: ")
        db.insert(name,sid,age,course)
      elif choice==3:
        db.showdatabase()
      elif choice==4:
        name=input("Enter the New Name: ")
        sid=input("Enter the SID: ")
        db.update(name,sid)
      elif choice==5:
        db.drop()
      elif choice==6:
        sid=input("Enter the SID to delete: ")
        db.delete(sid)
      elif choice==7:
        db.clause()
      elif choice==8:
        break
      else:
        print("")
        print("Invalid input")
    except Exception as e:
      print("")
      print("You entered invalid input")


main()