alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet *= 1000

def encrypt(original_text, shift_amount):
    encrypted_text = ''
    for letter in original_text.lower():
        if letter == ' ':
            encrypted_text += letter
        else:
            encrypted_text += alphabet[alphabet.index(letter) + shift_amount]
    
    print(encrypted_text)

def decrypt(encrypted_text, shift_amount):
    decrypted_text = ''
    for letter in encrypted_text:
        if letter == ' ':
            decrypted_text += letter
        else:
            decrypted_text += alphabet[alphabet.index(letter) - shift_amount]
    
    print(decrypted_text)

decrypt('cvmxjolbmfcjlvt difslj mpmpm vrjxfy', 1)
encrypt('Bulwinkalebikus Cherki LOLOl uqiwex',1)
