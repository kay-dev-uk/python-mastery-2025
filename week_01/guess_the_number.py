### Gues The Number ###

# It must generate a random number.

# It must take user input in a loop.

# It must provide "Too high" / "Too low" feedback.

# It must congratulate the user on success and terminate gracefully.

from random import randint

def guess_the_number():
    print("Welcome!")
    keep_playing = True
    while keep_playing:
        x = randint(1,10)
        user_guess = 0
        while user_guess != x and keep_playing:
            try:
                user_guess = int(input('Guess the number from 1 to 10: '))
                if(user_guess < x):
                    print('Too low!')
                elif(user_guess > x):
                    print('Too high!')
                else:
                    valid_response = False
                    while not valid_response:
                        user_response = str(input('Congrats! You won! Play again? Y/N: '))
                        if(user_response.lower() == 'y'):
                            valid_response = True
                            break
                        elif(user_response.lower() == 'n'):
                            keep_playing = False
                            valid_response = True
                            break
                        else:
                            print('Invalid Response. Enter Y or N')
                            pass
            except ValueError:
                print('It is not a valid response. Please, try again')
            except EOFError:
                print('\nExiting game...')
                keep_playing = False
                break
        if not keep_playing:
            break    



guess_the_number()
