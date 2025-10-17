alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet *= 1000

def caesar(direction, text, shift):

    if direction == 'encrypt':
        encrypted_text = ''
        for letter in text.lower():
            if letter == ' ':
                encrypted_text += letter
            else:
                encrypted_text += alphabet[alphabet.index(letter) + shift]
        
        print(encrypted_text)

    else:
        decrypted_text = ''
        for letter in encrypted_text:
            if letter == ' ':
                decrypted_text += letter
            else:
                decrypted_text += alphabet[alphabet.index(letter) - shift]
        
        print(decrypted_text)


caesar('encrypt','Bulwinkalebikus Cherki LOLOl uqiwex',1)
