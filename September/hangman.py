import random
word_list = ['aardvark', 'baboon', 'camel']

keep_playing = True

secret_word = random.choice(word_list)
display = len(secret_word) * '_'
guessed_letters = []

while keep_playing:
    
    print(display)

    guess = input('Guess the letter: \n').lower()
    if guess in secret_word:
        print('Correct!')
    else:
        print('Incorrect!')
    for letter in secret_word:
        if guess == letter:
            guessed_letters.append(guess)
    if len(guessed_letters) > 0:
        display = ''
        for i in secret_word:
            if i in guessed_letters:
                display += i
            else:
                display += "_"
    if '_' in display:
        keep_playing = True
    else:
        print('You won!')
        keep_playing = False


