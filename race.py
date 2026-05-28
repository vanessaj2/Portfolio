#Vanessa
#Race
#Simulates a race between a tortoise and hare

#Init
import random
finish_line = 50 #Finish Line
tortoise_pos = 0 #Starting Position
hare_pos = 0 #Starting Position
is_hare_asleep = False #Hare Starts Awake

#Functions
while tortoise_pos < finish_line and hare_pos < finish_line:
    tortoise_pos = tortoise_pos + random.randint(1,3)
    chance = random.randint(1,10)
    if chance <= 3:
        is_hare_asleep = True
        hare_pos = hare_pos
    elif chance >3:
        is_hare_asleep = False
        hare_pos = hare_pos + random.randint(1,10)
    print(f"Tortoise: {tortoise_pos} | Hare: {hare_pos}")
if tortoise_pos >= finish_line:
    print("🐢 The Tortoise wins!")
else:
    print("🐇 The Hare wins!")

#Main
