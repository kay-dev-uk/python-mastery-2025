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
    
    difficulty = input("Select difficulty 'easy' or 'hard':\n").lower()
    attempts = 10
    if difficulty == 'hard':
        attempts = 5
    keep_playing = True
    while keep_playing:
        secret_number = random.randint(1,100)
        print(secret_number)
        break

game()
