__author__ = 'Lada'

file = open("prob11.txt", "r")          # open file for reading

dt = []                              # initialize empty array
for line in file:
  dt.append(line.strip().split(' ')) # split each line on the <space>, and turn it into an array
                                      # thus creating an array of arrays.
file.close()

pmax=0

#
# for x in range(0,17):
#     # print(dt[0][x])
#     for y in range(0,17):
#         p1=int(dt[y][x])*int(dt[y][x+1])*int(dt[y][x+2])*int(dt[y][x+3])
#         p2=int(dt[y][x])*int(dt[y+1][x])*int(dt[y+2][x])*int(dt[y+3][x])
#         p3=int(dt[y][x])*int(dt[y+1][x+1])*int(dt[y+2][x+2])*int(dt[y+3][x+3])
#
#         pmax=max(p1,p2,p3,pmax)
#
# print("The solution is: " + str(pmax))


for x in range(0,17):
    # print(dt[0][x])
    for y in range(3,20):

        p3=int(dt[y][x])*int(dt[y-1][x+1])*int(dt[y-2][x+2])*int(dt[y-3][x+3])

        pmax=max(p3,pmax)

print("The solution is: " + str(pmax))