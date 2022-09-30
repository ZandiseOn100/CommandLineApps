import mysql.connector
import os
import maskpass

try:
    con = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    database = "syshelp",
    password = "Pass@2022"
    )
except:
    print("Could not establish a connection with the database") 


def initDB():
    mycursor = con.cursor()
    mycursor.execute("USE syshelp")


def displayMenu():
    print("#####################################")
    print(">> Welcome To SysHelp Main Menu")
    print("1. User Login")
    # print("2. Display Messages")
    print("2. Admin Login")
    print("3. Exit")
    print("#####################################")


def exit():
    user_input = int(input("Enter 4 to exit: "))
    if user_input == 4:
        os.system("cls")
        print("Goodbye!")
        quit()
    else:
        print("Invalid option!")
        exit()        


def loginUser():

    mycursor = con.cursor()
    print("Login")
    username = input("Enter username: ")
    if username == "":
        print("Username can't be empty!")
        return False
    password = maskpass.askpass("Enter password: ")
    if password == "":
        print("Password can't be empty!") 
        return False  

    mycursor.execute("SELECT * FROM sys_users WHERE username=%s AND password=%s", (username, password))
    user = mycursor.fetchall()

    if len(user) == 0:
        print("User doesn't exist, contact your admin!")
    else:
        print("User Info:")
        print(f"Welcome to the SysHelp Desk {user[0][1]}!")
        dashboardView()   
def dashboardView():

    print("--SysHelp Dashboard!--")
    
    print("The SysHelp provides you with the support and solutions you need to quickly resolve technical problems.")
    print("\n") 
    print(">> Select from the list")
   
    print("1. Submit an Incident")
    print("2. Submit a Request")
    print("3. FAQ")
    print("4. Exit")
    user_input = int(input("Enter option: "))
    
    if user_input == 1:
        title = input("Enter the title of the problem you have: ")
        if title == "":
            print("Title is required: ")
            return False 
        description = input("Enter the description of the problem: ")
        if description =="":
            print("Title is required: ")
            return False
        sql_stmt = "INSERT INTO incidents(TITLE, DESCRIPTION) VALUES(%s,%s)"
        val = (title, description)           
        mycursor = con.cursor()
        mycursor.execute(sql_stmt, val)
        con.commit()
        print("------------Submitted incident sucessfully!-------------")
        exit()
    elif user_input == 2:
        title_req = input("Enter the title of the problem you have: ")
        if title_req == "":
            print("Title is required: ")
            return False 
        description_req = input("Enter the description of the problem: ")
        if description_req =="":
            print("Title is required: ")
            return False
        sql_stmt = "INSERT INTO requests(TITLE, DESCRIPTION) VALUES(%s,%s)"
        val_req = (title_req, description_req)           
        mycursor = con.cursor()
        mycursor.execute(sql_stmt, val_req)
        con.commit()
        print("------------Submitted request sucessfully!-------------")
        exit() 
    elif user_input == 3:
        print("Getting the info.......")
        sql_stmt = "SELECT * from faq"
        mycursor = con.cursor()
        mycursor.execute(sql_stmt)
        info = mycursor.fetchall()
        print("Frequently asked question: ", info[0][0])
        print("Admin Answer: ", info[0][1])
    elif user_input == 4:
        print("Goodbye!")
        run()
    else:
        print("Invalid Input")
        run()   



def dashboardAdmin():
    print("---Admin Login---")
    mycursor = con.cursor()
    print("Login")
    username = input("Enter admin username: ")
    if username == "":
        print("Username can't be empty!")
        return False
    password = maskpass.askpass("Enter admin password: ")
    if password == "":
        print("Password can't be empty!") 
        return False  

    mycursor.execute("SELECT * FROM admin_users WHERE username=%s AND password=%s", (username, password))
    user = mycursor.fetchall()

    if len(user) == 0:
        print("User doesn't exist!")
    else:
        print("Welcome to the SysHelp Desk !")
        print("User Info: \n")
        print("---------------------------")  
        print("Administrators online ") 
        print(f"{user[0][1]}")
        print("---------------------------") 
    mycursor.execute("SELECT * FROM incidents")
    incident = mycursor.fetchall()

    if len(incident) == 0:
        print("No incidents!")
    else:    
         
        print("*****Help Desk Requests*****") 
        print("\n")
        for row in incident:
            print("Incident: \n-----Incident Number-----Title-----Incident Description \n", row)
        print("\n")
        print("---------------------------") 


    mycursor.execute("SELECT * FROM requests")
    request = mycursor.fetchall()

    if len(request) == 0:
        print("No requests!")
    else:    
         
        print("*****Help Desk Requests*****") 
        print("\n")
        for row in request:
            print("Request: \n----Request Number-----Title-----Request Description \n", row)
        print("\n")
        print("---------------------------")         


def run():

    displayMenu()
    user_input = int(input("Enter an option: "))
    if user_input == 1:
        os.system("cls")
        loginUser()
    elif user_input == 2:
        os.system("cls")
        dashboardAdmin()
    elif user_input == 3:
        os.system("cls") 
        print("Goodbye!")             
        quit()
    else:
        os.system("")
        run()


if __name__ == "__main__":
    initDB()
    run()
    
    
    