n=int(input())
res=1
cnt=0
for i in range(1,n+1,1):
    res *= i
a=list(map(int,str(res)))
for i in range(len(a),0,-1):
    if(a[i-1]==0):
        cnt+=1
    else:
        break
print(cnt)