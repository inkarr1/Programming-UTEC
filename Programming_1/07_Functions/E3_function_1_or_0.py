def function_x(x_limit):
    for x in range(0, x_limit + 1):
        if x >= x_limit/2:
            y = 1
        else:
            y = 0
        print(f"{x} -> {y}")
    return


function_x(100)
