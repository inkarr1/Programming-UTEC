def function_multiplos_10(x_input):
    i = 0
    while i < x_input:
        i += 1
        if i % 20 == 0:
            y = 1
            print(f"{i} -> {y}")
        else:
            y = 0
            print(f"{i} -> {y}")
    return


function_multiplos_10(100)
