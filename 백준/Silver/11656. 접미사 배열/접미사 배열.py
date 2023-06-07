s=input()
a=[s[i:] for i in range(len(s))]
a.sort()
print(*a,sep='\n')