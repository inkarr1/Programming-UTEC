n_input = int(input("Ingrese: "))
x_data = 1 / 2
multiplicando = 1
result_total = 0

if n_input == 0:
    n_input = 30


for i in range(n_input):
    divisor = (2 * i + 1)
    dividendo = (2 * i + 2)
    resultado = divisor / dividendo
    multiplicando *= resultado

    if i == 0:
        print(f"{divisor}/{dividendo} = {resultado}")
    elif i == 1:
        print(f"{divisor - 2}/{dividendo - 2} * {divisor}/{dividendo} = {multiplicando}")
    else:
        print(f"... * {divisor - 2}/{dividendo - 2} * {divisor}/{dividendo} = {multiplicando}")

    print("*" * 20)

    for x in range(1, n_input + 1):
        exponente = (2 * x + 1)
        result_expo = (x_data ** exponente) / exponente
        print(f"({x_data} ** {exponente}) / {exponente} = {result_expo}")

        print("-" * 20)

    result_multi = multiplicando * result_expo
    print(f"{multiplicando} * {result_expo} = {result_multi}")
    result_total += result_multi
    print(f"Suma n°{x} -> {result_total}")
    print("*" * 15)

print("^" * 15)

pi = 6 * (x_data + result_total)
print(f"6 * ({x_data} + {result_total}) = {pi}")
print(f"El resultado de serie n°{n_input} de pi por el arcsen es:", "{:.6f}".format(pi))


