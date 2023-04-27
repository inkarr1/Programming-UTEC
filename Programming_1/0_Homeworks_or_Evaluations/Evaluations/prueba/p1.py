nombre_paciente = input("NOMBRE DEL PACIENTE: ")
sexo_paciente = input("REGISTRAR SECO DEL PACIENTE: ")
altura_paciente = float(input("REGISTAR ALTURA (Mts.): "))

resultado_tidal_litros = 6 * (((50 * (sexo_paciente == "H")) + (45.5 * (sexo_paciente == "M"))) + 0.91 * ((altura_paciente * 100) - 152.4))

print("EL CALCULO DEL VOLUMEN TIDAL DEL PACIENTE", nombre_paciente, "ES:", "{:.2f}".format(resultado_tidal_litros), "mililitros")