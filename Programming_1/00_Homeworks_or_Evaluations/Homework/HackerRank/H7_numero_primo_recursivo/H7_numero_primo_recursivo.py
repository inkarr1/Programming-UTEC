def isPrime(number, divisor):
    if divisor == 1:
        return False
    elif number % divisor == 0:
        return True
    else:
        return isPrime(number, divisor - 1)


def isRecursivePrime(number):
    if number == 1:
        valor = False
    else:
        valor = isPrime(number, number - 1)

    result = "El numero " + str(number) + (" no" * valor) + " es primo."
    return result


number = int(input())
print(isRecursivePrime(number))

