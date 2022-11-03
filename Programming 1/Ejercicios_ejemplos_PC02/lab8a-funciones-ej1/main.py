def diasPorMes(mes=12, anio=2022):
    if mes==2:
        if anio%4==0:
            return 29
        else:
            return 28
    elif mes==4 or mes==6 or mes==9 or mes==11:
        return 30
    else:
        return 31

dia = int(input("Dia:"))
mes = int(input("Mes:"))
anio = int(input("Año:"))
diasAnioNuevo=0
if (mes!=12):
    diasAnioNuevo=diasPorMes(mes,anio) - dia
    for i in range(mes + 1, 13):
        diasAnioNuevo += diasPorMes(i,anio)
else:
    diasAnioNuevo = diasPorMes(anio=anio) - dia


print("Los dias que falta para año nuevo :",diasAnioNuevo)