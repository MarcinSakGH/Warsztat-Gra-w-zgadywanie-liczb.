from random import randint


comp_num = randint(1, 100)
while True:
    guess = input("Guess the number: ")
    try:
        guess = int(guess)
    except ValueError:
        print("It's not a number!")
        continue
    if guess < comp_num:
        print("Too small!")
        continue
    elif guess > comp_num:
        print("Too big!")
        continue
    else:
        print("You win!")
        exit()