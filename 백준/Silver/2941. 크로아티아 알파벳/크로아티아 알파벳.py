a=['c=','c-','dz=','d-','lj','nj','s=','z=']
n=input()
res=0
for i in a:
    n=n.replace(i,' ')
print(len(n))