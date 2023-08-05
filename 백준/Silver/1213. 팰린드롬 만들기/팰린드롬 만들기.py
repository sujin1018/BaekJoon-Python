from collections import Counter
n=list(input())
n.sort()
a=Counter(n)
cnt=0
mid,res='',''
for i in a:
    if a[i]%2==1:
        cnt+=1
        mid=i
        n.remove(i)
    if cnt>1:
        break
if cnt>1:
    print("I'm Sorry Hansoo")
else:
    for i in range(0,len(n),2):
        res+=n[i]
    print(res+mid+res[::-1])