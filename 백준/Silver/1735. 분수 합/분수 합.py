a,b=map(int,input().split())
c,d=map(int,input().split())
x=a*d+b*c
y=b*d
def gcd(i,j):
    while j>0:
        i,j=j,i%j
    return i
g=gcd(x,y)
if g!=1:
    x//=g
    y//=g
print(x,y)