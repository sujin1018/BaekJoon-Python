a=[i+1 for i in range(int(input()))]
b=[]
for i in range(len(a)):
    b.append(a.pop(0))
    if len(a)==0:
        break
    a.append(a.pop(0))
print(*b)