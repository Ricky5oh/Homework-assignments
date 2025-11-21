# Date: 07/22/25
# Homework 4:  Numeric Processing
# Program By:  Ricardo Duran
# File Name:   H4_Dec_Funcs.py
# Function:    This program reads and writes to files

# defining functions
def operation(func):
    """" Using Decortator that identifys the name of the math operation function"""
    def wrapper(x, y):
        print(f"\nPerforming {func.__name__}")
        return func(x, y)
    return wrapper

def verifying_operation(func):
    """" Verifying the users input before continuing """
    def calc(user_choice):
        if user_choice in [1,2,3,4,0]:
            return func(user_choice)
        else:
            print("Invalid Input !, Please try again")
            return None
    return calc

def Startup_Menu():
    """" Displaying the startup menu and returning users input"""
    print("\nEnter an Operation:\n")
    print("1 Add")
    print("2 Sub")
    print("3 Multiply")
    print("4 Divide")
    print("0 Quit")
    try:
        return int(input(">"))
    except ValueError:
        return -1
    
def get_operand():
    """" Prompting the user to enter a operand """
    while True:
        try:
            return int(input("\nEnter an operand: "))
        except ValueError:
            print("Invalid input. Please Enter a single integer value, ex.(1,2,3,4)")

@operation
def add(x, y):
    """" Returning the sum of x and y """
    return x + y
@operation
def sub(x, y):
    """" Returning the subtracted amount of x and y """
    return x - y
@operation
def mult(x, y):
    """" Returning the multiplyed answer of x and y """
    return x * y

@operation
def div(x, y):
    """" Returning the divided amount of x and y"""
    if y == 0:
        print("Invalid Input")
        return None
    return x / y

@verifying_operation
def calc(user_selection):
    """" Performing the operation by calling the operation functions """
    x = get_operand()
    y = get_operand()

    if user_selection == 1:
        result = add(x, y)
    elif user_selection == 2:
        result = sub(x, y)
    elif user_selection == 3:
        result = mult(x, y)
    elif user_selection == 4:
        result = div(x, y)
    else:
        result = None

    if result is not None:
        print(f"\nResult: {result}")   

# Looping the start up menu
def menu_loop():
    while True:
        choice = Startup_Menu()
        if choice == 0:
            print("Good Bye!")
            break
        calc(choice)

if __name__ == "__main__":
    menu_loop()    

test