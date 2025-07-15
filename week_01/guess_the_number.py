### Gues The Number ###

# It must generate a random number.

# It must take user input in a loop.

# It must provide "Too high" / "Too low" feedback.

# It must congratulate the user on success and terminate gracefully.

from random import randint

def guess_the_number():
    print("Welcome!")
    keep_playing = True
    x = randint(1,11)
    user_guess = 0
    while user_guess != x and keep_playing:
        user_guess = int(input('Guess the number from 1 to 10: '))
        if(user_guess < x):
            print('Too low!')
        elif(user_guess > x):
            print('Too high!')
        else:
            user_response = input('Congrats! You won! Play again? Y/N: ')
            if(user_response == 'y'):
                guess_the_number()
            else:
                keep_playing = False
                break

guess_the_number()
