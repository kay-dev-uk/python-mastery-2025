import random
word_list = ['aardvark', 'baboon', 'camel']

keep_playing = True

secret_word = random.choice(word_list)
display = len(secret_word) * '_'
guessed_letters = []
user_lives = 5

while keep_playing:
    
    print(display)
    print(f'Lives left: {user_lives}')

    guess = input('Guess the letter: \n').lower()
    if guess in secret_word:
        guessed_letters.append(guess)
        print('Correct!')
    else:
        print('Incorrect!')
        user_lives -= 1
        if user_lives == 0:
            print('You lost!')
            keep_playing = False

    if len(guessed_letters) > 0:
        display = ''
        for i in secret_word:
            if i in guessed_letters:
                display += i
            else:
                display += "_"
        if '_' not in display:
            print(secret_word)
            print('You won!')
            keep_playing = False


