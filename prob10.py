__author__ = 'Lada'


psum=2
plist=[2]

for x in range(2,2000000):
    prime=True
    for y in plist:
        if x%y==0:
            prime=False
            break
    if prime==True:
        print(x)
        plist.append(x)
        psum+=x

print("The solution is: " +str(psum))