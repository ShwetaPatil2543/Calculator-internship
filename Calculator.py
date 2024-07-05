def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculator():
    print("~~~~~ Mini Calculator ~~~~~")
    
    num1 = float(input("Enter the first number here: "))
    num2 = float(input("Enter the second number here: "))
    
    print("Press 1 for addition \nPress 2 for subtraction \nPress 3 for multiplication \nPress 4 for division")
    
    choice = int(input("Enter your choice from 1-4: "))
    
    if choice == 1:
        print("The addition of the given two numbers is:", add(num1, num2))
    elif choice == 2:
        print("The subtraction of the given two numbers is:", subtract(num1, num2))
    elif choice == 3:
        print("The multiplication of the given two numbers is:", multiply(num1, num2))
    elif choice == 4:
        print("The division of the given two numbers is:", divide(num1, num2))
    else:
        print("Invalid input")

calculator()
