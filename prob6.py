__author__ = 'Lada'

a=0
b=0
for x in range(1, 101):
    a += pow(x,2)
    b += x

b=pow(b,2)

print (a)
print (b)
print(b-a)
