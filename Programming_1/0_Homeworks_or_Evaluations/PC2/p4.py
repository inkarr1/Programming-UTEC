phrase = input("Ingrese la frase: ")

letter_replace = input("Ingrese una letra a reemplazar: ")
new_letter_replace = input("Ingrese la nueva letra: ")

new_phrase = phrase.replace(letter_replace, new_letter_replace)

print(new_phrase)