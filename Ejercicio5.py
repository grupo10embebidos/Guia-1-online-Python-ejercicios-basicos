# Problema 5

print("Ingrese la edad de la primera persona")
edad1 = int(input())
print("Ingrese la edad de la segunda persona")
edad2 = int(input())

if edad1 < edad2:
    print("La primera persona es más joven")
elif edad1 > edad2:
    print("La segunda persona es más joven")
else:
    print("Ambas personas tienen la misma edad")