n_input = int(input("Ingrese: "))

x_data = 1 / 2
multiplicando = 1
result_total = 0

if n_input == 0:
    n_input = 30


for i in range(n_input):
    divisor = x_data ** (2 * (i+1) + 1)
    dividendo = (2 * (i+1) + 1)
    resultado = divisor / dividendo
    result_expo = 1
    for x in range(1, (i+1)*2, 2):
        result_expo *= x / (x+1)
        print("\t", result_expo)

    result_multi = resultado * result_expo
    result_total += result_multi
    print(result_total)


pi = 6 * (x_data + result_total)
print(f"6 * ({x_data} + {result_total}) = {pi}")
print(f"El resultado de serie n°{n_input} de pi por el arcsen es:", "{:.6f}".format(pi))