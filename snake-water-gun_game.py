import random

print("Welcome to Snake-Water-Gun Game")

list = ["S", "W", "G"]
r = random.choice(list)
i = 10
c = 0
p = 0
while(i > 0 and i < 11):
    str = input(
        "Enter your choice\nEnter S for snake, W for water and G for game\n")
    if(str == "S" and r == "W"):
        print("The player has entered", str, "and computer has entered",
              r, "So player wins")
        i = i - 1
        p = p + 1
        print("Number of attempts left", i)
    elif(str == "S" and r == "G"):
        print("The player has entered", str, "and computer has entered",
              r, "So computer wins")
        i = i - 1
        c = c + 1
        print("Number of attempts left", i)
    elif(str == "W" and r == "S"):
        print("The player has entered", str, "and computer has entered",
              r, "So computer wins")
        i = i - 1
        c = c + 1
        print("Number of attempts left", i)
    elif(str == "W" and r == "G"):
        print("The player has entered", str, "and computer has entered",
              r, "So player wins")
        i = i - 1
        p = p + 1
        print("Number of attempts left", i)
    elif(str == "G" and r == "S"):
        print("The player has entered", str, "and computer has entered",
              r, "So computer wins")
        i = i - 1
        c = c + 1
        print("Number of attempts left", i)
    elif(str == "G" and r == "W"):
        print("The player has entered", str, "and computer has entered",
              r, "So computer wins")
        i = i - 1
        c = c + 1
        print("Number of attempts left", i)
    else:
        print("The Game is Tie please start again")
        i = i - 1
        print("Number of attempts left", i)
if(i == 0):
    print("You have 0 attempts left, Game Over!!")

if(p > c):
    print("The wins of the player is", p, " and wins of computer is",
          c, "So the player has won the game")
elif(p < c):
    print("The wins of the player is", p, " and wins of computer is", c,"and computer has won the game")
else:
    print("The Game has been tied")
