def function_x(x_limit):
    y = 0
    for x in range(0, x_limit + 1):
        if 11 > x >= 0:
            print(f"{x} -> {y}")
        elif 20 >= x:
            y += 1
            print(f"{x} -> {y}")
        elif 30 >= x:
            y += 2
            print(f"{x} -> {y}")
    return


function_x(100)
