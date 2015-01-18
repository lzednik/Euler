__author__ = 'Lada'
import math

solved=False
tn=0
nn=1
maxcounter=0

while solved==False:
   tn+=nn
   nn+=1

   flist=[]
   fcounter=0

   for d in range(1,int(math.ceil(tn/2))):
    if tn%d==0 and flist.__contains__(d)!=True:
        flist.append(d)
        fcounter+=1

        if fcounter>maxcounter:
            maxcounter=fcounter
            print("So far the winner is " + str(tn) +" with "+str(maxcounter)+ " divisors")

        if fcounter==500:
            print("The final solution is: " +str(tn))
            solved=True