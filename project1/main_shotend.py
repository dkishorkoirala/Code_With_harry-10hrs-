import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")

youDict = {"s": 1, "w": -1, "g":0}
reverseDict = {1: "Snake", -1 : "Water", 0:"Gun"}

you = youDict[youstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")
if (computer == you ):
    print("Its draw")

else:
    '''
    if (computer == -1 and you == 1): (computer - you) = -2
        print ("You win!")

    elif(computer == -1 and you == 0): (computer - you) = -1
        print("You lose!")

    elif (computer ==1 and you == -1): (computer - you) = 2
        print("You loose!!")

    elif (computer == 1 and you == 0):(computer - you) =  1
        print("You win!")

    elif(computer == 0 and you == -1): (computer - you) = 1
        print("You win!")

    elif(computer == 0 and you == 1): (computer - you) = -1
        print("you loose!")

        
    the below logic is writeen on the basis of computer minus you (computer - you)
    '''
    if (computer - you ) == -1 or (computer - you ) == 2:
        print("You loose")
    else:
        print("You win")