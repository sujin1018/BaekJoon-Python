def d(n):
    n+=sum(map(int,str(n)))
    return n
ns=set()
for i in range(1,10001):
    ns.add(d(i))
for i in range(1,10001):
    if i not in ns:
        print(i)