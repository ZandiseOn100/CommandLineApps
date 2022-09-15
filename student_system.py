import mysql.connector
import os
import re
import maskpass


con = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    database = "studentsystem",
    password = "Pass@2022"
)

def initDB():
    mycursor = con.cursor()
    mycursor.execute("USE studentsystem")


def displayMainMenu():
    print("***********************************") 
    print(">> Main Menu")
    print("1. User Registration")
    print("2. User Login")
    print("3. Exit")
    print("***********************************") 


def exit():
    user_input = int(input("Enter 5 to exit: "))
    if user_input == 5:
        os.system("cls")
        print("Goodbye!")
        quit()
    else:
        print("Invalid option!")
        exit()

def registerUser():
     
    mycursor = con.cursor()
    print("-----* User Registration *----")
    first_name = input("Enter your name: ")
    if first_name == "":
        print("Name must be filled out")
        return False
    last_name = input("Enter your last name: ")
    if last_name == "":
        print("Last name must be filled out")
        return False    
    student_no = input("Enter your student number: ")
    if student_no == "":
        print("Student no must be filled out")
        return False    
    username = input("Enter your username: ")
    if username == "":
        print("Username must be filled out")
        return False    
    email = input("Enter your email: ")
    pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
    
    if email == "":
        print("Email must be filled out")
        return False
    elif re.match(pat, email):
        return True
    else:
        print("Email format wrong, re enter you email!")
        quit()          
    password = maskpass.askpass("Enter your password: ")
    if password == "":
        print("Password  must be filled out")
        return False    
    

    sql_stmt = "INSERT INTO users(FIRST_NAME,LAST_NAME,STUDENT_NO,USERNAME,EMAIL,PASSWORD) VALUES(%s,%s,%s,%s,%s,%s)"
    val = (first_name,last_name,student_no,username,email,password)

    mycursor.execute(sql_stmt, val)
    con.commit()
    print("------------Registered sucessfully!-------------")
    exit()    

def loginUser():
    mycursor = con.cursor()
    print("-----* User Registration *----") 
    username = input("Enter your username: ")
    if username == "":
        print("Username must be filled out")
        return False      
    password = maskpass.askpass("Enter password: ") 
    if password == "":
        print("Password  must be filled out")
        return False 
    mycursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password,))
    user = mycursor.fetchall()

    if len(user) == 0:
        print("User does't exist, try registering!")
    else:
        print("User Info")
        print("Welcome: ", user[0][1])  
        print("\n")



def run():
    displayMainMenu()
    n = int(input("Enter option: "))
    if n == 1:
        os.system("cls")
        registerUser()
    elif n == 2: 
        os.system("cls")
        loginUser()   
    elif n == 3: 
        os.system("cls")
        exit()       
    else:
        os.system("cls")
        run()                  


if __name__ == "__main__":
    initDB()
    run()