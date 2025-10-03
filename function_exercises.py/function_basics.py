import math


def print_hello():
    Print("hello")


def get_hello():
    return print_hello()


def ask_name_and_greet_user():
   name = input("What is your name: ")
   capitalized_name = name.capitalize()
   if name == "Thanos":
       print("Get out of here, Thanosw! Nobody wants to play with you!")
       
   else:
       print("Hi," + capitalized_name, ". Would you like to have a Hamburger")
    
    
def calculate_hypotenuse_lenght(a: float,b: float) -> float:
    return math.sqrt(a ** 2 + b ** 2)


def calculate_cathetus_lenght(a: float, c: float) -> float:
    math.sqrt(c ** 2 - a ** 2)

    