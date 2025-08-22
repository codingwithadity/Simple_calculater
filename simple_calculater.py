def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

  #user input
     x = float(input("enter first number: "))
     y = float(input("enter second number: "))
     
     
     print("addition ", add(x, y))    
     print("subtraction ", subtract(x, y))    
     print("multiply", multiply(x, y))    
     print("divide", divide(x, y))    