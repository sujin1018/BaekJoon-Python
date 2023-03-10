n = input()
d = dict()

for i in list(n.upper()):
    d[i] = d.get(i,0) + 1

res = [k for k,v in d.items() if max(d.values()) == v]
if(len(res) > 1):
    print("?")
else:
    print(res[0])
