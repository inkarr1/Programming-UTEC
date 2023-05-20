word = input("Ingrese la palabra: ")
word = word.lower()
lenght = len(word)

if lenght > 3:
    if word[-3:] == "ing":
        word += "ly"
    else:
        word += "ing"
print(word)
