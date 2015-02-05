__author__ = 'Lada'

def amic(a):
    sumd=0
    for i in range(1,a):
        if a%i==0:
           sumd+=i
    return sumd


l=[]
sumamic=0
for x in range(1,10000):
    y=amic(x)
    if x==amic(y):
        if x not in l:
            l.append(x)
            sumamic+=x

print("The solution is: " + str(sumamic))