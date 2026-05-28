#Vanessa
#Hogwarts
#Create a program that prompts the user for their name and simulates being assigned one of the 4 hogwarts houses

#Functions
import time
import random

def main():
    print("Welcome to Hogwarts")
    name = input("Please enter a name: ")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    print(house(name))

def house(name):
    if name == "Harry" or name == "Ron" or name == "Hermione":
        name = "Gryffindor"
    if name == "Newt" or name =="Nymphadora" or name =="Pomona":
        name = "Hufflepuff"
    if name == "Luna" or name == "Cho" or name == "Filius":
        name = "Ravenclaw"
    if name == "Voldemort" or name == "Draco" or name == "Severus":
        name = "Slytherin"
    else:
        name = int(random.randint(1,4))
        if name == 1:
            name = "Gryffindor"
        if name == 2:
            name = "Hufflepuff"
        if name == 3:
            name = "Ravenclaw"
        if name == 4:
            name = "Slytherin"
    return name

#Main
main()
