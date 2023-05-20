string_1 = input("Ingrese string 1: ")
string_2 = input("Ingrese string 2: ")

new_a = string_2[:2] + string_1[2:]
new_b = string_1[:2] + string_2[2:]

print(new_a + ' ' + new_b)
