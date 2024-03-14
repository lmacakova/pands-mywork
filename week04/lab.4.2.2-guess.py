number = 8
guess= int(input("Please, guess a number: "))
while guess != number:
    print("Wrong.")
    guess = int(input("Please, guess a number, again: "))
print ("Well, done. The number was ", number)