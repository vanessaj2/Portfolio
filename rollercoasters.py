#Purpose: This program helps users decide which rollercoaster is best for them based on their preferences
#CoasterFinder

#Initialize
import pandas as pd
import random
import webbrowser
import time

data = pd.read_csv('Rollercoasters.csv')

location = data['Amusement Park'].tolist()
city = data['City'].tolist()
country = data['Country'].tolist()
height = data['Height'].tolist()
speed = data['Speed'].tolist()
length = data['Length'].tolist()
rollercoaster = data['Rollercoaster Name'].tolist()

#Images of coasters
image = ["https://rcdb.com/aadatre", "https://tinyurl.com/2s47yp8r",
         "https://tinyurl.com/4p243rvf","https://tinyurl.com/2kw5pkfz"]
#Research array during user input
search = []
#Categories of rollercoaster
kiddie = []
family = []
mega = []
hyper = []
#Categories of speed types according to the category of rollercoaster
slow = []
moderate = []
fast = []
extreme = []
#List for ride duration
short = []
average = []
long_ = []
extremely_long = []

#Functions
#This menu allows users to choose between 6 options
def menu():
    print("Welcome to CoasterFinder. Use our program to help you find a rollercoaster that best fits your needs.")
    organize()
    while True:
        ask = input("Do you want a recommendation for a rollercoaster ride (Yes, No): ").lower()
        if ask == "yes":
            options = input("Choose an option to filter by: Your Stats (Age), Rollercoaster Speed (Speed), Height of Ride (Height), Duration (Time), Generate (g), or Exit (e): ").lower()
            if options == "age":
                age = int(input("How old are you?: "))
                if age <= 3: #This if statement ends the program if the user's age is less than or equal to 3.
                    print("Sorry, you are too young to ride a rollercoaster.")
                    break
                elif age > 3:
                    height_age(age)
            elif options == "speed":
                rate = input("What rollercoaster speed are you comofrtable with? (Slow, Moderate, Fast, Extreme): ").lower() #This input becomes the value passed into the parameter for the function speeds
                speeds(rate)
            elif options == "height":
                type = input("How high up do you want to go: (Kiddie, Family, Mega, Hyper) ").lower()
                ride_height(type)
            elif options == "time":
                time = input("How long do you want your ride to last? (Short, Average, Long, Extremely Long): ").lower()
                duration(time)
            elif options == "g":
                generate()
            elif options == "e":
                print("We're sad to see you go. We hope to see you again!")
                break
        elif ask == "no": #If the user responds "no" to the question, they unlock 2 additional filter choices; researching a coaster or getting a popular recommendation
            searching = input("Do you want to research about a rollercoaster instead? (Yes, No) ").lower()
            if searching == "yes":
                name = input("Please enter the name of the rollercoaster you want to learn more about: ")
                research(name)
            elif searching == "no":
                popular = input("There are a few popular recommendations most of our users end up choosing. Would you like to learn more? (Yes, No): ").lower()
                if popular == "yes":
                    view = input("What kind of popular rollercoaster are you interested in viewing? (Kiddie, Family, Mega, Hyper): ").lower()
                    popular_choices(view)
                elif popular == "no":
                    print("Thank you for using CoasterFinder.")
                    break
        else: #This statement handles invalid inputs
            print("That's not an option! Please try again.")
            continue

def height_age(age):
    if age >3: #This function only works if the user's age is greater than 3 and proceeds to ask about heights using if statements
        heigh = float(input("How tall are you in feet? (3-3.5, 3.6-4.5, 4.6-7): "))
        if 3 <= heigh <= 3.5:
            print("Great! You are tall enough to ride the kiddie coaster!")
            print(f"We recommend the {random.choice(kiddie)}, a kiddie rollercoaster less than 26 feet tall.")
        elif 3.5 < heigh <= 4.5:
            print("Great! You are tall enough to ride the family coaster!")
            print(f"We recommend the {random.choice(family)}, a family rollercoaster between 26 and 60 feet tall.")
        elif heigh > 4.5:
            print("Great! You are able to ride the mega and hyper coasters!")
            type = input("Do you want to ride the mega rollercoaster (mega) or hyper rollercoaster (hyper)?: ")
            if type == "mega":
                print(f"We recommend the {random.choice(mega)}, a mega rollercoaster between 60 and 100 feet tall.")
            elif type == "hyper":
                print(f"We recommend the {random.choice(hyper)}, a hyper rollercoaster between 100 and 130 feet tall.")
        else:
            print("Please enter your height.")

def speeds(rate):
    for i in range(len(rollercoaster)):
        if speed[i] <= 30:
            slow.append(rollercoaster[i])
        elif speed[i] > 30 and speed[i] <=65:
            moderate.append(rollercoaster[i])
        elif speed[i] > 65 and speed[i] <= 100:
            fast.append(rollercoaster[i])
        elif speed[i] > 100:
            extreme.append(rollercoaster[i]) #This filters the rollercoasters in the data set into specific arrays depending on their speeds
    if rate == "slow": #Once the users passes an argument into the parameter rate, they get recommended a random choice from an array
        rand_slow = random.choice(slow)
        print(f"We recommend the {rand_slow} rollercoaster. This rollercoaster goes very slowly, perfect for beginners or those afraid of high speeds.")
    elif rate == "moderate":
        rand_mod = random.choice(moderate)
        print(f"We recommend the {rand_mod} rollercoaster. This moderately paced rollercoaster is the perfect sweet spot between fast and slow.")
    elif rate == "fast":
        rand_fast = random.choice(fast)
        print(f"We recommend the {rand_fast} rollercoaster. This rollercoaster is suitable for experienced riders.")
    elif rate == "extreme":
        rand_extreme = random.choice(extreme)
        print(f"We recommend the {rand_extreme} rollercoaster. This rollercoaster is extremely fast, so ride carefully.")

def ride_height(type):
    if type == "kiddie":
        print(f"We recommend the {random.choice(kiddie)}, a kiddie rollercoaster less than 26 feet tall.")
    elif type == "family":
        print(f"We recommend the {random.choice(family)}, a family rollercoaster between 26 and 60 feet tall.")
    elif type == "mega":
        print(f"We recommend the {random.choice(mega)}, a mega rollercoaster between 60 and 100 feet tall.")
    elif type == "hyper":
        print(f"We recommend the {random.choice(hyper)}, a hyper rollercoaster between 100 and 130 feet tall.")

def duration(time):
    for i in range(len(rollercoaster)):
        if length[i] >= 60 and length[i] <= 300:
            short.append(rollercoaster[i])
        elif length[i] > 300 and length [i] <= 600:
            average.append(rollercoaster[i])
        elif length[i] > 600 and length[i] <=1200:
            long_.append(rollercoaster[i])
        elif length[i] > 1200:
            extremely_long.append(rollercoaster[i])
    if time == "short":
        print(f"We recommend the {random.choice(short)}. This ride will last approximately 1 minute. ENJOY!")
    elif time == "average":
        print(f"We recommend the {random.choice(average)}, This ride will last approximately 2-3 minutes. ENJOY!")
    elif time == "long":
        print(f"We recommend the {random.choice(long_)}, This ride will last approximately 4-5 minutes. ENJOY!")
    elif time == "extremely long":
        print(f"We recommend the {random.choice(extremely_long)}, This ride will last approximately 6-8 minutes. ENJOY!")

#Assigns rollercoasters into an array depending on their category
def organize():
    for i in range(len(rollercoaster)):
        if height[i] <=26:
            kiddie.append(rollercoaster[i])
        elif height[i] >=26.1 and height[i]<=60:
            family.append(rollercoaster[i])
        elif height[i] >=61.1 and height[i] <= 100:
            mega.append(rollercoaster[i])
        elif height[i] >= 100.1 and height[i] <= 130:
            hyper.append(rollercoaster[i])

#Allows users to learn more about a specific roller coaster
def research(name):
    for i in range(len(rollercoaster)):
        if name in rollercoaster[i]:
            print(data.loc[i])

#Provides a randomly generated rollercoaster from the database
def generate():
    print("Choosing a rollercoaster. Please wait a moment.")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    coaster = random.choice(rollercoaster)
    print(f"We recommend the {coaster}.")

def popular_choices(view):
    if view == "kiddie":
        webbrowser.open(image[0])
        print(data.loc[36])
        print("This is the Coccinelle, a kiddie rollercoaster located in Roquefort, Aquitaine in France.")
        print("This coaster is a chill ride for those who are frightened by heights.")
    elif view == "family":
        webbrowser.open(image[1])
        print(data.loc[118])
        print("This is the Giant Dipper, a family rollercoaster located in Santa Cruz, USA.")
        print("It's near the beach and reaches moderate heights, making it great for people who want some fun without the adrenaline rush.")
    elif view == "mega":
        webbrowser.open(image[2])
        print(data.loc[247])
        print("This is the Goliath, a mega rollercoaster located in Valencia, USA.")
        print("This coaster reaches towering heights, but is a great step below hyper rollercoasters for more experienced riders.")
    elif view == "hyper":
        webbrowser.open(image[3])
        print(data.loc[252])
        print("This is the Top Thrill Dragster, a hyper rollercoaster located in Sandusky, USA.")
        print("This coaster is great for brave riders, prepared for terrifying heights and constant movement!")
#Main
menu()

#Sources
#Rollercoaster Dataset
#Website Name: Code.org
#URL: https://tuvalabs.com/datasets/?type=datasets&order_by=-pub_date&show=all
#Dataset Source: https://tuvalabs.com/datasets/?type=datasets&order_by=-pub_date&show=all

#Coccinelle Kiddie Rollercoaster
#Website Name: RCDB
#Photographers: https://rcdb.com/about.htm
#URL: https://rcdb.com/946.htm

#Giant Dipper Family Coaster
#Website Name: Secret San Francisco
#Author: Jamie Ferrell
#URL: https://secretsanfrancisco.com/santa-cruz-boardwalk-giant-dipper/
#Date: November 15, 2021

#Goliath Mega Rollercoaster
#Title: It’s hard to top Goliath at Six Flags Great America
#Website Name: AboutThemeParks
#Author: Arthur Levine
#URL: https://www.aboutthemeparks.fun/p/its-hard-to-top-goliath-at-six-flags
#Date: July 20, 2023

#Rollercoaster Top Thrill Dragster Hyper Coaster
#Title: Cedar Point fans determined to uncover secrets behind Top Thrill Dragster's new design
#Website Name: Detroit Free Press
#Author: Frank Witsil
#URL: https://www.freep.com/story/news/local/michigan/2023/07/30/top-thrill-dragster-cedar-point-ohio-clues-amusement-park/70419761007/?gnt-cfr=1&gca-cat=p&gca-uir=false&gca-epti=z114301u115701e1122xxv114301&gca-ft=245&gca-ds=sophi
#Date: July 28, 2023
