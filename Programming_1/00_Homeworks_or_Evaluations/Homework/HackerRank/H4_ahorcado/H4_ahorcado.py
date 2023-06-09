def hangman_mecanics(word, letter_guessed):
    guessed_word = ''
    for letter in word:
        if letter in letter_guessed:
            guessed_word += letter
        else:
            guessed_word += '-'
    return guessed_word


def hangman_play():
    word_input = input("")
    print("Inicia el juego:)")
    print(f"La palabra tiene {len(word_input)} letras:")
    print("-" * len(word_input))

    guess_done = 0
    guess_total = len(word_input) + 1
    print(f"Tienes {guess_total} intentos")

    letter_guessed = ""

    while True:
        guess_done += 1
        guess_letter = input("")
        letter_guessed += guess_letter
        guessed_word = hangman_mecanics(word_input, letter_guessed)
        print(f"Intento {guess_done} :")
        print(guessed_word)

        if guessed_word == word_input:
            print("Te salvaste!")
            break

        if guess_done >= guess_total:
            print("Estas ahorcado!")
            break


hangman_play()
