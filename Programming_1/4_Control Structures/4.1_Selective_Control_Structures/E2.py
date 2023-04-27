serie_range = int(input("n: "))
i = 1
serie_sum = 0

while serie_range >= i:
    serie_sum = serie_sum + i ** 2
    # print(serie_item)
    i = i + 1
print("suma:", serie_sum)
