unidades = {
    "platano": 6,
    "manzana": 0,
    "naranja": 32,
    "pera": 15
}
precios = {
"platano": 4,
"manzana": 2,
"naranja": 1.5,
"pera": 3
}

# frutas = input("ingresar lista:")
frutas = "pera ,naranja ,pera"
listaFrutas = frutas.split(",")

total = 0
for elem in listaFrutas:
    if unidades[elem.strip()]>0:
        unidades[elem.strip()] -= 1
        total += precios[elem.strip()]

print(unidades)
print("total:",total)