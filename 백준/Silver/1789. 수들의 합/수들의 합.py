s=int(input())
n,res=0,0
for i in range(1,s+1):
    res+=i
    n+=1
    if(res>s):
        n-=1
        break;
print(n)