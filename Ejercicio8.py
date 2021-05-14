# Problema 8

print("Ingrese varA")
varA = input()
print("Ingrese varB")
varB = input()

error = 0
try:
    int(varA)
except ValueError:
    print('string involucrado')
    error = 1
    
if error == 0:
    if varA > varB:
        print('mas grande')
    elif varA < varB:
        print('mas pequeño')
    else:
        print('igual')