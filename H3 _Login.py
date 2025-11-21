# Date: 07/15/25
# Homework 3: User Login
# Program By: Ricardo Duran
# File Name: H3_Login.py
# Function: This program will authenticate user access

#User Information Dictionary 
users = { 
    1: {"username": "Mikey", "password": "pizzatime", "role": "standard"},
    2: {"username": "Donny", "password": "halfshell", "role": "standard"},
    3: {"username": "Raph", "password": "shredhead", "role": "standard"},
    4: {"username": "Leo", "password": "cowabunga", "role": "admin"}
}
#User Greeting
print("Hello!\n")
#Verifying if the user already has a account created
choice = input("Do you have an account? \n" ">")
    
user_list = list(users.values())

if  choice.upper()== 'Y': #Added the 'upper' in choice incase of lower case 'y'
    username = input("Please enter in your username:\n" ">")
    password = input("Please enter in your password:\n" ">")
    correct_account = False
#Checking through the dictionary to see if the username and password are a match
    for user_id, user_info in users.items():
        if user_info['username'] == username and user_info ['password'] == password:
            correct_account = True
            print("Thank you, your information was found!\n\n")        
            if user_info["role"] == "admin":
                print ("ADMIN ACCESS GRANTED: Welcome to the Secret Sewer System!\n")
                print ("Here are the current users:\n")
                print ("UserID" + "  "+ "Username" + "  "+ "Password" + "  " + "Role\n")
                for user_id,user_info in users.items():
                    print( f"{user_id}\t{user_info['username']}\t {user_info['password']}\t{user_info['role']}\n")
            else:
                print("ACCESS GRANTED: Welcome to the Secret Sewer System!\n")
            break

    if not correct_account:
        print("Sorry, your information was NOT Found!")
        print("ACCESS DENIED!")
#If user does not have a account, it will prompt them to create a new account
elif choice.upper() == 'N': #Added the 'upper' in choice incase of lower case 'n'
    new_username = input("Please enter in your desired username:\n" ">")
    new_password = input("Please enter in your desired password: \n" ">")
    new_id = max(users.keys()) + 1 # Checking existing user IDs and adding a new User ID 
    users[new_id] = {"username": new_username, "password": new_password, "role": "standard"} # Adding the new user to the User Dictionary
    print("Thank you, your information has been stored.\n")
    print("Access Granted: Welcome to the Secret Sewere System!\n")

else:
    print("Invalid input. Please enter Y or N.") # This is added incase another letter other then 'Y' or 'N' is entered, it will return a invalid character message

    test