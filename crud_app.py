import mysql.connector
import os
import maskpass

try:
    con = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    database = "crudopps",
    password = "Pass@2022"
    )
except:
    print("Could not establish a connection with the database") 


def initDB():
    mycursor = con.cursor()
    mycursor.execute("USE crudopps")
    

def displayMenu():
    print("#####################################")
    print(">> Welcome To College App Main Menu")
    print("1. Add Student")
    print("2. View Student Marks")
    print("3. Update Student Marks")
    print("4. Delete Student")
    print("5. Exit")
    print("#####################################")


def exit():
    user_input = int(input("Enter 5 to exit: "))
    if user_input == 5:
        os.system("cls")
        print("Goodbye!")
        quit()
    else:
        print("Invalid option!")
        exit() 
 
def addRec():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    marks = int(input("Enter student marks: "))
    mycursor = con.cursor()
    sql_stmt = "INSERT INTO student(NAME, AGE, MARKS) VALUES(%s, %s, %s)"
    val = (name, age, marks)
    mycursor.execute(sql_stmt,val)
    con.commit()

    print('------ SUCCESSFULLY ADDED! ------\n')
    exit()
   

def viewRec():
    mycursor = con.cursor()
    mycursor.execute("SELECT * FROM student")
    student = mycursor.fetchall()

    if len(student) == 0:
        print("No info!")
    else:    
         
        print("*****Student Info*****") 
        print("\n")
        for row in student:
            print("Student : \n-----Student Name----- Age-----Marks \n", row)
        print("\n")
          

def updateRec():
    print("------ INFO BEFORE UPDATE! ------\n")
    viewRec()
    id = int(input("Enter student id: "))
    marks = int(input("Update student marks: "))
    mycursor = con.cursor()
    sql_stmt = "UPDATE student SET MARKS=%s WHERE ID=%s"
    update_data = (marks, id)
    mycursor.execute(sql_stmt,update_data)
    con.commit()
    print("------ UPDATE ADDED! ------\n")
    
    print("------ INFO UPDATED! ------\n")
    mycursor.execute("SELECT * FROM student")
    student = mycursor.fetchall()

    if len(student) == 0:
        print("No info!")
    else:    
         
        print("*****Updated Info*****") 
        print("\n")
        for row in student:
            print("Student : \n-----Student Name----- Age-----Marks \n", row)
        print("\n")
        print("---------------------------")  
    exit() 
def delRec():
    print("------ INFO BEFORE DELETE! ------\n")
    viewRec()
    id = int(input("Enter student id to delete: "))
    mycursor = con.cursor()
    sql_stmt = "DELETE FROM student WHERE ID=%s"
    delete_data = (id)
    mycursor.execute(sql_stmt,(delete_data,))
    con.commit()
    print("------ STUDENT DELETED! ------\n")
    
    print("------ UPDATED INFO! ------\n")
    mycursor.execute("SELECT * FROM student")
    student = mycursor.fetchall()

    if len(student) == 0:
        print("No info!")
    else:    
         
        print("*****Updated Info*****") 
        print("\n")
        for row in student:
            print("Student : \n-----Student Name----- Age-----Marks \n", row)
        print("\n")
        print("---------------------------")  
    exit()
               
#calling the main menu        
def run():

    displayMenu()
    user_input = int(input("Enter an option: "))
    if user_input == 1:
        os.system("cls")
        addRec()
    elif user_input == 2:
        os.system("cls")
        viewRec()
    elif user_input == 3:
        os.system("cls")
        updateRec()
    elif user_input == 4:
        os.system("cls")
        delRec()    
    elif user_input == 5:
        os.system("cls") 
        print("Goodbye!")             
        quit()
    else:
        os.system("")
        print("Invalid option, please select from the list provided")
        run()
    
if __name__ == "__main__":
    initDB()
    run()
    