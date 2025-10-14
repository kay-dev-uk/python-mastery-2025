alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet *= 1000

def encrypt(original_text, shift_amount):
    # def get_position(letter, amount):
    #     if (alphabet.index(letter) + shift_amount) > len(alphabet - 1)


    encrypted_text = ''
    for letter in original_text.lower():
        if letter == ' ':
            encrypted_text += letter
        else:
            encrypted_text += alphabet[alphabet.index(letter) + shift_amount]
    
    print(encrypted_text)

encrypt('Bulwinkalebikus Cherki LOLOl uqiwex',1)
