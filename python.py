import random
score= random.randint(1,1000)
guess = 0
user = -1
while user!=score:
    user = int (input("enter your number"))
    guess+=1
    if user>score:
        print ("lower number please")

    elif user<score:
        print ("higher number please")

    else:
        print (f"congratulations you have won the game in {guess} attempts")