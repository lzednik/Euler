__author__ = 'Lada'

maxcounter=1

for n in range(10,1000000):
    counter=1
    ntemp=n

    while ntemp!=1:
        if ntemp%2==0:
            ntemp=ntemp/2
        else:
            ntemp=3*ntemp+1
        counter+=1

    if counter>maxcounter:
        maxcounter=counter
        print("The current max is " +str(maxcounter) +" when n is "+str(n))



