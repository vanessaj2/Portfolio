#Vanessa
#Image Generator
#Provides recommendations for pets after answering a series of questions

#Init
import webbrowser

#Functions
url = ["https://tinyurl.com/4xp3wvup", #Black Lab
       "https://tinyurl.com/5dut94z2", #Fish
       "https://www.rd.com/wp-content/uploads/2019/11/cat-10-e1573844975155-scaled.jpg?fit=750%2C750", #Cat
       "https://newagepet.com/cdn/shop/articles/pet-lizard-tongue.jpg?v=1755713282&width=1100" #Lizard
       ]

desc = [ "Dogs are the perfect companion for family time. Because they are highly energetic animals, you will spend a lot of time playing with them.",
        "Fishes are low-maintenance pets, and you can watch them from their tank.",
        "Cats can be cuddly and friendly, making them great pets to chill with. They can be independent, so you won't spend as much time with them" ,
        "Lizards are calm, friendly animals, so they can walk outside of their enclosure, and require more maintenance than fishes." ]


def pets():
    play = input("Do you like playful animals? (yes, no): ")
    if play == "yes":
        time = input("Would you like to spend a lot of time with your pet? (yes,no): ")
        if time == "yes":
            webbrowser.open(url[0])
            print(desc[0])
        elif time == "no":
            webbrowser.open(url[2])
            print(desc[2])
    elif play == "no":
        cute = input("Would you like to pet your animal? (yes, no): ")
        if cute == "yes":
            webbrowser.open(url[3])
            print(desc[3])
        elif cute == "no":
            webbrowser.open(url[1])
            print(desc[1])


#Main
pets()


#Sources Information

#Picture of black lab dog
#Website Name: The Guardian
#Author: Sarah Phillips
#URL:https://www.theguardian.com/lifeandstyle/2025/apr/27/which-dog-should-i-get-how-to-choose-the-best-pet-for-families-city-living-or-people-with-allergies
#Article Title: Which dog should I get? How to choose the best pet for families, city living or people with allergies
#Date: April 27, 2025

#Picture of fish
#Website Name: Aqueon
#Author: n/a
#URL: https://www.aqueon.com/articles/ways-to-know-your-fish-are-happy
#Article Title:5 Ways to Know Your Fish Are Happy and Healthy
#Date: n/a

#Picture of cat
#Website Name: Reader's Digest
#Author: Morgan Cutolo
#URL: https://www.rd.com/list/common-cat-myths/
#Article Title: 14 Common Cat Myths You Probably Believed Were True—Until Now
#Date: May 09, 2025

#Picture of lizard
#Website Name: New Age Pet
#Author: n/a
#URL: https://newagepet.com/blogs/learning-center/what-you-need-to-know-about-keeping-a-lizard-as-a-pet
#Article Title: What You Need To Know About Keeping A Lizard As A Pet
#Date: Aug 20, 2025
