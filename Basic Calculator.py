""" Build a basic calculator that can perform operations like addition, subtraction, 
multiplication, and division. This will give you practice with functions and control 
flow. """

inp=input("Enter a number: ")
inp2=input("Enter a number: ")

operation=input("Enter an operation: ")
if operation == "+":
    result = float(inp) + float(inp2)
    print (f"result: {result}")
elif operation == "-":
    result = float(inp) - float(inp2)
    print (f"result: {result}")
elif operation == "*":
    result = float(inp) * float(inp2)
    print (f"result: {result}")
elif operation == "/":
    result = float(inp) / float(inp2)
    print (f"result: {result}")
else:
    print("Invalid operation")
    result = None


