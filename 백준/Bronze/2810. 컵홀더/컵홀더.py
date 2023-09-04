n=int(input())
a=input()
l=a.count('LL')
if l<=1:
    print(n)
else:
    print(n-l+1)