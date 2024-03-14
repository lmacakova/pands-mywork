import random
number = random.randint(0,100)
guess =int(input("Please, guess a number: "))
while guess != number:
    if guess < number: 
        print("Too low.")
        guess = int(input("Please, guess a number, again: "))
    else:
        print("Too high.")
        guess = int(input("Please, guess a number, again: "))
print ("Well, done. The number was ", number)