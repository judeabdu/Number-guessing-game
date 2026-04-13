import random
secret_number = random.randint(1,50)
print("       Number should be btwn 1 and 50 inclusive     ")
print("              you have 10 trials                    ")
print("                  Debug number:", secret_number)
for trial in range(1,11):
    Guess = int(input("\n Enter your guess number btwn 1 and 50: "))
    if Guess < 1 or Guess > 50:
        print("Ur guess is beyond range:")
    else:
        print(f"Good, ur guess is {Guess} which is")
    difference = abs(Guess - secret_number)
    if Guess == secret_number:
        print("\nCorrect, U won")
        break
    elif Guess > secret_number:
        if difference > 10:
            print("way too high")
        else:
            print("too high")
    elif Guess < secret_number:
        if difference > 10:
            print("way too low")
        else:
            print("too low")
else:
    print("Game Over, Try later, the number was:", secret_number)
