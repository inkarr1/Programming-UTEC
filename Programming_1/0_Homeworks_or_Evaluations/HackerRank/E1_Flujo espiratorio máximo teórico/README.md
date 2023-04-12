# Flujo espiratorio másximo teórico
El Flujo espiratorio máximo (PEF por sus siglas en inglés) es la velocidad máxima de 
espiración de una persona que se mide con un dispositivo de mano utilizado para 
monitorear la capacidad de una persona para exhalar aire. En la literatura médica se 
utiliza un cálculo teórico que está dado por las siguientes expresiones:

Si la paciente es Mujer:

```PEF(litros/seg) = 0.0448 * Talla(cm) - 0.0304 * Edad + 0.35```

Si el paciente es Hombre:

```PEF(litros/seg) = 0.0945 * Talla(cm) - 0.0209 * Edad - 5.77```

Se le solicita desarrollar un programa que realice el cálculo del PEF. Para los datos de 
entrada va a recibir el siguiente formato:

- Sexo: El caracter H para Hombre y M para Mujer:
- Edad: Valor entero
- Talla: Valor decimal en metros

### Input Format
```
M
30
1.52
```
### Constraints
No se puede utilizar estructuras de control, solo debe utilizar expresiones.
### Output Format
```EL CALCULO PEF TEORICO ES: 6.2476 ( litros/seg )```
### Sample Input 0
```
M
30
1.52
```
### Sample Output 0
```EL CALCULO PEF TEORICO ES: 6.2476```
### Sample Input 1
```
M
35
1.78
```
### Sample Output 1
```EL CALCULO PEF TEORICO ES: 10.3195```
