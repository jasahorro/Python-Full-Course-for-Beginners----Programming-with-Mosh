# ask a user their weight in pounds
# and convert it to kilograms and print it out

""" weight = input("weight in pounds: ")
befloat = float(weight)

befloat = befloat * 0.45359237

print("weight in kilograms: " + str(befloat)) """

""" course = "python for beginners"
print(len(course))
print(course.upper())
print(course.find("p"))
print(course.replace("p", "j")) """

#guessing game
""" import random
guess = input(("guess a number between 1 and 10: "))

guessint = int(guess)
realnum = random.randint(1,10)

if guessint == realnum:
    print("you guessed it right!")
else:
    print("you guessed it wrong!")
     """

#car game

""" car = input("> ")

while car != "quit":
    car = input("> ").lower()
    if car  == "start":
        print("car started")
    elif car == "stop":
        print("car stopped")
    elif car == "help":
        print("start - to start the car")
        print("stop - to stop the car")
        print("quit - to exit the game")
    elif car == "quit":
        print("you quit the game")
    else:
        print("sorry, I don't understand") """

#shopping cart
""" prices = [10, 20, 30]
total= 0
for i in prices:
    total += i
print(total) """

""" for x in range (4):
    for y in range (3):
        print(f"({x}, {y})") """

#F shape 
""" number = [5, 2, 5, 2, 2]
for n in number:
    if n == 5:
        print ("xxxxx")
    else:
        print ("xx")
     """

# find largest number

""" numbers = [3,6,2,8,4,10]
max = numbers[0]
for n in numbers:
    if n > max:
        max = n
print(max) """

# remove duplicates 
""" numbers = [2,2,4,6,3,4,6,1]
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique) """

# digits to words
""" cp = input("enter a phone number: ")

digits = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "zero"
}

for ch in cp:
   digits.get(ch, ch) # if the character is not in the dictionary, it will return the character itself
   print(digits.get(ch, ch), end=" ") """

# oop classes
""" class Person:
    def __init__(self, name): #this is a constructor parang attribute sya 
        self.name = name

    def talk (self): # this is a method, parang function sya pero sa loob ng class
        print(f"hi, I am {self.name}")

mj = Person("mj")
mj.talk()
 """
# oop inheritance 

class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal): # Dog is a subclass of Mammal
    pass

class Cat(Mammal): # Cat is a subclass of Mammal
    def walk(self):
        print("cat walkingg....")

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.walk()