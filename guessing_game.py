import random
while True:
    number = random.randint(1,75)
    print("Guess a number between 1 and 75")
    guess = int(input())

    if guess == number:
        print("You win!")
    else:
        if guess < number:
            print("Tool low"
        elif guess > number:
            print("Tool high!")
        print(f"Wrong!The number was {number}")
    
    print("Play again? (y/n)")
    if input().lower() != 'y':
        break;
