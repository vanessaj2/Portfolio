#Vanessa
#Todo
#Grocery list that the user can interact with

#Functions

#Main
list = ["Onions", "Garlic", "Chicken", "Eggs", "Beef", "Bread"]
done = []

def grocery_list():
    print(f"See your grocery list: {list}")
    while True:
        option = input("What would you like to do? (Add, Complete, Remove, Clear, Exit) ").lower()
        if option == "add":
            add = input("What item would you like to add? ").capitalize()
            list.append(add)
            print(f"Here is your current grocery list: {list}")
            print(f"Here is your checked off list: {done}")
        if option == "complete":
            print(f"Here is your current grocery list: {list}")
            complete = input("What item would you like to mark complete? ").capitalize()
            list.remove(complete)
            done.append(complete)
            print(f"Here is your current grocery list: {list}")
            print(f"Here is your checked off list: {done}")
        if option == "remove":
            item = input("What item would you like to remove? ").capitalize()
            try:
                list.remove(item)
                print(f"Here is your current grocery list: {list}; {item} has been removed.")
                print(f"Here is your checked off list: {done}")
            except:
                print("That's not an option.")
                continue
        if option == "clear":
            list.clear()
            print(f"Here is your current grocery list: {list}")
        if option == "exit":
            print(f"Here is your current grocery list: {list}")
            print(f"Here is your checked off list: {done}")
            break

#Main
grocery_list()
