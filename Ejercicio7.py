# Problema 7

import os
from decimal import *

getcontext().prec = 1500

sumador = 0

for n in range(1,10000,1):
    sumador += pow(-1,n+1)/Decimal((2*n)*(2*n+1)*(2*n+2))
    
pi = (sumador * 4) + 3 
print(pi)