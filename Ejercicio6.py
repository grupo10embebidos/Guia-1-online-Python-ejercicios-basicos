# Problema 6

print("Ingrese el primer numero")
num1 = float(input())
print("Ingrese el segundo numero")
num2 = float(input())
num1 = pow(num1,2)


if num1 < num2:
    print("El segundo es mayor que el cuadrdo del primero")
elif num1 > num2:
    print("El segundo es menor que el cuadrado del primero")
else:
    print("El segundo es el cuadrado exacto del primero")