number = 0
while number <= 0 or number > 500:
    number = int(input("Número [1 - 500]: "))

i = 0
while i < number:
    i += 1
    if i % 4 == 0 and i % 6 == 0:
        print(i, "TicTac")
    elif i % 6 == 0:
        print(i, "Tac")
    elif i % 4 == 0:
        print(i, "Tic")
    else:
        print(i)