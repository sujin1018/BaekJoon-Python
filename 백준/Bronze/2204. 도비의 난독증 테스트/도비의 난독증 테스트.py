while True:
    n=int(input())
    if n==0:
        break
    a=[input() for _ in range(n)]
    a.sort(key=str.lower)
    print(a[0])