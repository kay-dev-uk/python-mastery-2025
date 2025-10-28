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
    
    
    while keep_playing:
        difficulty = input("Select difficulty 'easy' or 'hard':\n").lower()
        attempts = 10
        if difficulty == 'hard':
            attempts = 5
        keep_playing = True
        secret_number = random.randint(1,100)
        secret_number_guessed = False
        while not secret_number_guessed and attempts > 0:
            user_guess = input(f"Guess the number. You have {attempts} attempts left:\n")
        

game()
