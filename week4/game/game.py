import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        pass
    else:
        if level < 1:
            pass
        else:
            break

rand_num = random.randint(1, level)

guessed = False

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess < 1:
            pass
        else:
            if guess > rand_num:
                print("Too large!")
            elif guess < rand_num:
                print("Too small!")
            else:
                print("Just right!")
                break
