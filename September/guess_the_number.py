# Guess The Number
# Ask for difficulty easy or hard
# Hard: 5 tries
# Easy: 10 tries
# Upon guess if not correct print higher or lower

# def prime(num):
#     if num < 2:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True
    


# print(prime(90))
import random
def game():
    keep_playing = True
    
    while keep_playing:
        difficulty = input("Select difficulty 'easy' or 'hard':\n").lower()
        attempts = 10
        if difficulty == 'hard':
            attempts = 5
        
        secret_number = random.randint(1,100)
        secret_number_guessed = False
        while not secret_number_guessed and attempts > 0:
            user_guess = int(input(f"Guess the number between 1 and 100. You have {attempts} attempts left:\n"))
            if user_guess < secret_number:
                print("Think higher")
                attempts -= 1
                if attempts == 0:
                    print("You lost!")
                    break
            elif user_guess > secret_number:
                print("Think lower")
                attempts -= 1
                if attempts == 0:
                    print("You lost!")
                    break
            else:
                print(f"You won! You guessed the number {secret_number}")
                secret_number_guessed = True
                break
        user_choice = input("Play again? y/n:\n").lower()
        if user_choice == "y":
            continue
        else:
            break
        

game()
