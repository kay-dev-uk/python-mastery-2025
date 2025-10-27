# Guess The Number
# Ask for difficulty easy or hard
# Hard: 5 tries
# Easy: unlimited
# Upon guess if not correct print higher or lower

def prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
    


print(prime(90))
