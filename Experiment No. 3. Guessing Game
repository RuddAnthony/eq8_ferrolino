import random

random_number = random.randint(1,100)
attempt = 10

for i in range(attempt):
    guess = int(input("Guess a number from 1 to 100: "))
        
    if (guess == random_number):
        print("correct")
        print("Total Guesses Used:", i+1)
        break
    
    elif (guess > random_number):
        print("too high")
        print("attempts left:", attempt - (i+1))
            
    elif (guess < random_number):
        print("too low")
        print("attempts left:", attempt - (i+1))
    
else:
    print("The Number was:", random_number)
