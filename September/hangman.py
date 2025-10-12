import random
word_list = ['aardvark', 'baboon', 'camel']

keep_playing = True




while keep_playing:
    secret_word = random.choice(word_list)
    show_word = ''
    guess = input('Guess the letter: \n')
    if guess in secret_word:
        print('Right')
    else:
        print('Wrong')
