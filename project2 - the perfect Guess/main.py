import random
n = random.randint(1,100)
a = -1
guesses = 1
while (a != n):
    a = int(input("Guess a number: "))

    if (a > n):
        print("Too high, lower number please")
        guesses += 1
        
    elif(a < n):
        print("Too low, higher number please")
        guesses += 1
    
print(f"You have guessed the correct number {n} in {guesses} attempts")