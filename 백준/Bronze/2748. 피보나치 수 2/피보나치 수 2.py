n=int(input())
a=[0]*1000
def f(n):
    if n<=1:
        return n
    if a[n] != 0:
        return a[n]
    a[n]=f(n-1)+f(n-2)
    return a[n]
print(f(n))