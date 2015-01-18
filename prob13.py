__author__ = 'Lada'

file = open("prob13.txt", "r")          # open file for reading

dt = []                              # initialize empty array
for line in file:
  dt.append(line.strip().split(' ')) # split each line on the <space>, and turn it into an array
                                      # thus creating an array of arrays.
file.close()


sumx=0
for x in range(0,100):
    sumx+=int(dt[x][0])

print(str(sumx)[0:10])