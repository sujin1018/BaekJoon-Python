import sys
input = sys.stdin.readline
x_coor, y_coor = {}, {}
for _ in range(int(input())):
    x,y = map(int,input().split())
    if x in x_coor:
        x_coor[x] += 1
    else:
        x_coor[x] = 1
    if y in y_coor:
        y_coor[y] += 1
    else:
        y_coor[y] = 1
count = 0
for i in x_coor:
    if x_coor[i] > 1:
        count += 1
for i in y_coor:
    if y_coor[i] > 1:
        count += 1
print(count)