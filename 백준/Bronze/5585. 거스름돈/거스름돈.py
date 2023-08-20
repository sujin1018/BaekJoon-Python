n=1000-int(input())
m=[500,100,50,10,5,1]
cnt=0
for i in m:
    cnt+= n//i
    n%=i
print(cnt)