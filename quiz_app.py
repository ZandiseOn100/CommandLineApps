import maskpass
import hashlib
import re


#signup 
def signup():
    """
    Registers a user to the system
    """
    email = input("Enter your email: ")
    pwd = maskpass.askpass("Enter password: ")
    conf_pwd = maskpass.askpass("Re-enter password: ")
    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    if re.fullmatch(regex, email):
        print("Valid email")
    elif email == "":
        print("Email must not be empty!")
        quit()
    else:
        print("Invalid email")
        quit()
    if pwd == "":
        print("Password must not be empty!")
        quit()  
    elif conf_pwd !="" and conf_pwd == pwd:
        encpwd = conf_pwd.encode()
        hash1 = hashlib.md5(encpwd).hexdigest()

        with open("usercredentials.txt", "w") as f:
            f.write(email + "\n")
            f.write(hash1)
        f.close
        print("You have registered successfully!")
    else:
        print("Password is not the same as above! \n")  

#login
def login():
    """
    Logs in  a user to the system
    """
    email = input("Enter your email: ")
    pwd = maskpass.askpass("Enter password: ")

    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("usercredentials.txt", "r") as f:
        stored_email, stored_pwd = f.read().split("\n")
    f.close()
    if email == stored_email and auth_hash == stored_pwd:
        print("Logged in successfully!")
        print("Welcome to the console system, you'll play a quiz game based of friends sitcom! \n")

        while True:
            #game section
            score = 0
            user_question = input("Do you want play a game(yes/no)? ").lower()

            if user_question == "yes":
                print("Loading game.....")
            else:
                print("Goodbye!") 
                quit()
            print("Let's play F•R•I•E•N•D•S Quiz Game!")
            print("A. Bird")   
            print("B. Dog")  
            print("C. Snake")   
            print("D. Monkey")
            print("Q. Quit")                          
            user_quiz =  input("What pet did Ross own? ").lower()

            if user_question == "a":
                print("Incorrect")
            elif user_quiz == "b":
                print("Incorrect!")
            elif user_quiz == "c":
                print("Incorrect!")                                
            elif user_quiz == "d":
                print("Correct!")
                score += 1
            elif user_quiz =="quit":
                print("Goodbye!")  
                quit()
            else:
                print("Unknown error occured!")  
                quit()

            print("A. Bricklaying")   
            print("B. Cooking")  
            print("C. American football")   
            print("D. Singing")
            print("Q. Quit")
            user_quiz =  input("What is Monica skilled at? ").lower()

            if user_question == "a":
                print("Incorrect")
            elif user_quiz == "b":
                print("Correct!")
                score += 1
            elif user_quiz == "c":
                print("Incorrect!")                                
            elif user_quiz == "d":
                print("Inorrect!")
            elif user_quiz =="quit":
                print("Goodbye!")  
                quit()
            else:
                print("Unknown error occured!") 
                quit()

            print("A. Sally Roberts")   
            print("B. Amy Welsh")  
            print("C. Valerie Thompson")   
            print("D. Emily Foster")
            print("Q. Quit")
            user_quiz =  input("Rachel was popular in high school. Her prom date Chip ditched her for which girl at school? ").lower()

            if user_question == "a":
                print("Incorrect")
            elif user_quiz == "b":
                print("Correct!")
                score += 1
            elif user_quiz == "c":
                print("Incorrect!")                                
            elif user_quiz == "d":
                print("Inorrect!")
            elif user_quiz =="quit":
                print("Goodbye!")  
                quit()
            else:
                print("Unknown error occured!") 
                quit()

            print("A. Snowflake")   
            print("B. Waddle")  
            print("C. Huggsy")   
            print("D. Bobber")
            print("Q. Quit")
            user_quiz =  input("What’s the name of Joey’s penguin? ").lower()

            if user_question == "a":
                print("Incorrect")
            elif user_quiz == "b":
                print("Incorrect!")
            elif user_quiz == "c":
                print("Correct!")  
                score += 1                              
            elif user_quiz == "d":
                print("Inorrect!")
            elif user_quiz =="quit":
                print("Goodbye!")  
                quit()
            else:
                print("Unknown error occured!") 
                quit()
            
            percetage = (score / 4) * 100    
            print(f"You got {score} questions")  
            print(f"That evaluates to {percetage} %.")                  

    else:
        print("Login failed! \n")

while True:
    print("------------------->Login System<----------------------")
    print("1.Signup")    
    print("2.Login") 
    print("3.Exit") 
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        signup()
    elif user_choice == 2:
        login()
    elif user_choice == 3:
        print("Goodbye.....")
        break
    else:
        print("Wrong choice!")  