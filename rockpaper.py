import random
Game = ["rock", "paper", "scissors"]
print("Game starts ")
n = 0
Computer = 0
User = 0
while n <= 5:
    cmp = random.choice(Game)
    Player = None
    while Player not in Game:
        Player = input("rock,paper,scissors : ").lower()
    if Player == cmp:
        print("Computer : ",cmp)
        Computer += 1
        User += 1
        print("Tie!")
    elif Player == "rock":
        if cmp == "paper":
            print("Computer : ", cmp)
            print("Computer gets a point ")
            Computer += 1
        if cmp == "scissors":
            print("Computer : ", cmp)
            print("Player  gets a point ")
            User += 1
    elif Player == "paper":
        if cmp == "scissors":
            print("Computer : ", cmp)
            print("Computer gets a point ")
            Computer += 1
        if cmp == "rock":
            print("Computer : ", cmp)
            print("Player  gets a point ")
            User += 1

    elif Player == "scissors":
        if cmp == "rock":
            print("Computer : ", cmp)
            print("Computer gets a point ")
            Computer += 1
        if cmp == "paper":
            print("Computer : ", cmp)
            print("Player  gets a point ")
            User += 1
    n += 1
print("Game is over the scores are\ncomputer : {} \n User : {} ".format(Computer,User))
if(Computer>User):
    print("Computer won the game !")
elif(Computer < User):
    print("user  won the game !\n Sorry better luck next time\n")
else:
    print("Game tie!")
    
    
# This is a comment

