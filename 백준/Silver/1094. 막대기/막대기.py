x=int(input())
s=[64,32,16,8,4,2,1]
cnt=0
for i in range(len(s)):
    if x==0:
        break
    if x>=s[i]:
        x-=s[i]
        cnt+=1
print(cnt)