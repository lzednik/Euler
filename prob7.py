__author__ = 'Lada'
import math

solved=False

num=5
pcount=2

while solved==False:
    x=1
    xsum=0
    notprime=False
    prime=False
    while x <= int(math.ceil(num/2)) and notprime==False:
        x += 1

        if num%x ==0:
            notprime=True

        if x==int(math.ceil(num/2)):
            prime=True


    if prime==True:
        pcount += 1

        print("Found Prime: " + str(num)+ " Prime Count is: " + str(pcount))
        if pcount==10001:
            print("solution is:" +str(num))
            solved=True

    num += 1
