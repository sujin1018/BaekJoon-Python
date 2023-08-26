n=input()
f=int(input())
res=int(n[:-2]+'00')
while True:
    if res%f==0:
        break
    res+=1
print(str(res)[-2:])