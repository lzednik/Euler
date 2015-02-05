__author__ = 'Lada'

import math

a= math.factorial(100)

a=str(a)
b=0

for i in range(0,len(a)-1):
   b+=int(a[i])

print"The solution is: " + str(b)
