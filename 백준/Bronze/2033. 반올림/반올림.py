n=int(input())
a=10
while n>a:
    tmp=n%a
    if tmp>=a//2:
        n+=a
    n-=tmp
    a*=10
print(n)