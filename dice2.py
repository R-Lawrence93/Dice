import random 

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll 


while True:
    players = input("Enter Number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else: 
             print("Must be between 2-4 players.")
    else:
        print("Invalid, try again")

player_one = 0
player_two = 0
player_tree = 0
player_four = 0

max_score = 50

print("player 1 your turn!")

should_roll = input("Would you like to roll (y)?")
    
if should_roll.lower() == "y":
       
    value = roll()
    if value != 1:
        print("You rolled a ", value)
        
        player_one+=value
        
        print("current score:", player_one)

    else:
         player_one = 0 
         print("You rolled a 1! Unlucky! Current score: ", player_one)
        
        
print("player 2 Turn")

should_roll = input("Would you like to roll (y)?")

if should_roll.lower() == "y":
    value = roll()
if value != 1:
        print("You rolled a ", value)
        
        player_one+=value
        
        print("current score:", player_two)

else:
         print("You rolled a 1! Unlucky! Current score: ", player_one)




    