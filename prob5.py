__author__ = 'Lada'

solved=False
num=20

while solved==False:
    xsum=0
    for x in range(1, 20):
        xsum=xsum+num%x

    if xsum==0:
        print("The answer is:" + str(num))
        solved=True
    else:
        num=num+1