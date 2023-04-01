s=[0]*9
n=input()
for i in n:
    i=int(i)
    if i==9:
        i=6
    s[i]+=1
s[6]=(s[6]+1)//2
print(max(s))