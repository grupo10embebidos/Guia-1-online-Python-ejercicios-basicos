# Ejercicio 11

print('Ingrese numero')
num = int(input())

sumador = 0
for n in range(1,num,1):
    print(f"{n} + ", end="")
    sumador += n
    
print(f"= {sumador}")