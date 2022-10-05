# CIFRADO CESAR
# Importar libreria para no hacer una lista de 'A' a la 'Z'
import string
alphabet = list(string.ascii_uppercase)

# CIFRAR MENSAJE

# Ingresar mensaje que deseo cifrar:
phrase = input("Ingrese mensaje a cifrar: ")

# Function para cifrar un mensaje:
def caesar_cipher(alphabet,position,text):
    text_cipher = ""
    for letter in text:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            caesar_index = current_index + position
            if caesar_index > 25:
                caesar_index -= 25
            text_cipher += alphabet[caesar_index]
        else:
            text_cipher += letter
    return text_cipher

phrase_cipher = caesar_cipher(alphabet,1,phrase)
print("Frase cifrada:", phrase_cipher)


# DECIFRAR EL MENSAJE

# Ingresar mensaje que deseo decifrar:
phrase_to_cipher= input("Ingrese frase a decifrar: ")

# Function para decifrar un mensaje:
def decifrar(alfabeto,position,text):
    text_decryption = ""
    for letter in text:
        if letter in alfabeto:
            caesar_index = alfabeto.index(letter)
            original_index = caesar_index - position
            if original_index < 0:
                original_index += 25
            text_decryption += alfabeto[original_index]
        else:
            text_decryption += letter
    return text_decryption

phrase_decryption = decifrar(alphabet,1,phrase_to_cipher)
print("Frase decifrada:", phrase_decryption)