__author__ = 'Lada'
import math

for a in range(1,1000):
    for b in range(a+1,1001):
        c=pow(a,2)+pow(b,2)
        if math.sqrt(c)==math.floor(math.sqrt(c)):
            #print("a="+str(a)+"b="+str(b)+"c="+str(c))
            if (a+b+math.sqrt(c))==1000:
                print("a="+str(a)+"b="+str(b)+"c="+str(math.sqrt(c)))
                print(a*b*math.sqrt(c))
