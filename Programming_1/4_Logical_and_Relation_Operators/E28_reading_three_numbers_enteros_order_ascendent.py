number_1 = int(input("Número 1: "))
number_2 = int(input("Número 2: "))
number_3 = int(input("Número 3: "))

last_number = max(number_1, number_2, number_3)
first_number = min(number_1, number_2, number_3)
second_number = number_1 + number_2 + number_3 - last_number - first_number

print(str(first_number) + ", " + str(second_number) + ", " + str(last_number))