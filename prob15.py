__author__ = 'Lada'

import math

n=40

l=[]

for k in range(0,n+1):
    c=math.factorial(n)/(math.factorial(k)*math.factorial(n-k))
    l.append(c)

print max(l)
