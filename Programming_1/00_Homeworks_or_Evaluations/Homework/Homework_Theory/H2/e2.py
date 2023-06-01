def pregunta_2(contrasenas: str) -> str:
    cantidad_validas = 0
    cantidad_invalidas = 0
    lista_validas = []

    contrasenas = contrasenas.split("/")

    caracteres_especiales = ["-", "*", "?", "!", "@"]

    for contrasena in contrasenas:
        if len(contrasena) < 8:
            cantidad_invalidas += 1
            continue

        tiene_mayuscula = False
        for letra in contrasena:
            if letra.isupper():
                tiene_mayuscula = True
                break

        if not tiene_mayuscula:
            cantidad_invalidas += 1
            continue

        if not any(letra.islower() for letra in contrasena):
            cantidad_invalidas += 1
            continue

        tiene_caracter = False
        for letra in contrasena:
            if letra in caracteres_especiales:
                tiene_caracter= True
                break

        if not tiene_caracter:
            cantidad_invalidas += 1
            continue

        if " " in contrasena:
            cantidad_invalidas += 1
            continue

        cantidad_validas += 1

        lista_validas.append(contrasena)


    return cantidad_validas, cantidad_invalidas, lista_validas


contra = input("contrasenas: ")
print(pregunta_2(contra))

# Ut3c111?/123456789/S3r3n4 D3 L30n@/NothingElseMatters1*!/LimaPeru1
# estaesunacontrasena / Comput3rCci3nc3 / programacion1-2023
# contrasena1/contrasena2/Contrasena3-/contrasena4/contrasena5


"""
        for letra in contrasena:
            if not letra.isupper():
                cantidad_invalidas += 1
                break
            if not letra.islower():
                cantidad_invalidas += 1
                break
            if not letra in caracteres_especiales:
                cantidad_invalidas += 1
                break
                
                if not any(letra in caracteres_especiales for letra in contrasena):
            cantidad_invalidas += 1
            continue
"""