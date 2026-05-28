#Vanessa and Allison
#Slots
#three slots casion machine game

#Init
import random

#Functions
symbols = ["7", "✨", "💓", "✿", "💓", "💓", "💓", "💓", "💓", "💓", "✿", "✿", "✿", "✨", "✨"]
roll = []
balance = 0
winnings = 0
credit_spent = 0
sim_spent = 0
jackpot = 0

def play():
    global balance
    begin = input("Welcome to the 3-slot Machine! What would you like to do? (Simulate 1000 plays (s) or Start Spinning (S): ")
    if begin == "s":
        simulation()
    elif begin == "S":
        if balance < 10:
            insufficient = input(f"You don't have enough credits to spin: You have {balance} credits. Add credits? (Yes, No): ").lower()
        if insufficient == "yes":
            wallet()
        elif insufficient == "no":
            print("You can't play.")
            exit

def wallet():
    global balance
    funds = input("How much would you like to add? (20,50,100): ")
    if funds == "20":
        balance = balance + 20
        print(f"You just bought {balance} credits!")
    elif funds == "50":
        balance = balance + 50
        print(f"You just bought {balance} credits!")
    elif funds == "100":
        balance = balance + 100
        print(f"You just bought {balance} credits!")
    else:
        print("Invalid")
        return
    game()

def game():
    global balance
    global winnings
    global credit_spent
    while True:
        question = input("Would you like to spin? One spin is 10 credits. (Yes (y), No (n), Cash out (c): ").lower()
        if question == "n":
            break
        if question == "y":
            balance = balance - 10
            for i in range(3):
                roll.append(random.choice(symbols))
            print(roll)
            if roll[0] == "7" and roll[1] == "7" and roll[2] == "7":
                winnings = winnings + 500
                balance = balance - 10
                credit_spent = 10 + credit_spent
                print("JACKPOT! You WON 500 credits!")
                print(f"You have {balance} credits left. You have used {credit_spent} credits. You have won {winnings} credits.")
            elif roll[0] =="✨" and roll[1] == "✨" and roll[2] == "✨":
                balance = balance - 10
                winnings = winnings + 100
                credit_spent = 10 + credit_spent
                print("You WON 100 credits!")
                print(f"You have {balance} credits left. You have used {credit_spent} credits. You have won {winnings} credits.")
            elif roll[0] == "💓" and roll[1] == "💓" and roll[2] == "💓":
                winnings = winnings + 100
                balance = balance - 10
                credit_spent = 10 + credit_spent
                print("You WON 100 credits!")
                print(f"You have {balance} credits left. You have used {credit_spent} credits. You have won {winnings} credits.")
            elif roll [0] == "✿" and roll[1] == "✿" and roll[2] == "✿":
                winnings = winnings + 100
                balance = balance - 10
                credit_spent = 10 + credit_spent
                print("You WON 100 credits!")
                print(f"You have {balance} credits left. You have used {credit_spent} credits. You have won {winnings} credits.")
            else:
                print("You lose")
            roll.clear()
        if question == "c":
            print(f"You have claimed {winnings} credits. See you next time!")
            break
        if balance < 10:
            print("You don't have enough balance. Add more to continue playing.")
            wallet()

def simulation():
    global credit_spent
    global roll
    global symbols
    global sim_spent
    global jackpot
    print("Simulation Starting...")
    simulation_win = 0
    for i in range(1000):
        sim_spent = sim_spent + 10
        symbols = ["7", "✨", "💓", "✿", "💓", "💓", "💓", "💓", "💓", "💓", "✿", "✿", "✿", "✨", "✨"]
        roll = random.choices(symbols, k=3)
        if roll[0] == "7" and roll[1] == "7" and roll[2] == "7":
            jackpot = jackpot + 1
            simulation_win = simulation_win + 100000
        elif roll[0] =="✨" and roll[1] == "✨" and roll[2] == "✨":
            simulation_win = simulation_win + 100
        elif roll[0] == "💓" and roll[1] == "💓" and roll[2] == "💓":
            simulation_win = simulation_win + 100
        elif roll[0] == "✿" and roll[1] == "✿" and roll[2] == "✿":
            simulation_win = simulation_win + 100
        roll.clear()
    print(f"Total Jackpots: {jackpot}")
    print(f"Total Credits Spent: {sim_spent}")
    print(f"Total Credits Won: {simulation_win}")
    print(f"Net Profit: {sim_spent - simulation_win}")
    play()

#Main
play()
