""" Build a unit converter that can convert between different units of measurement 
(e.g., kilometers to miles, Celsius to Fahrenheit). This project will strengthen your 
understanding of functions and user input. """

init = input("enter the unit you want to convert from: ")
init = init.lower()
try: 
    if init == "kilometers":
        kmtom = input("enter the distance in kilometers: ")
        kmtom = float(kmtom)
        kmtom = kmtom * 0.621371
        print(f"the distance in miles is {kmtom}")
    elif init == "celsius":
        celsius = input("enter the temperature in celsius: ")
        celsius = float(celsius)
        celsius = (celsius * 9/5) + 32
        print(f"the temperature in fahrenheit is {celsius}")
    else:
        print("invalid input")
except ValueError:
    print("please enter a valid number")







