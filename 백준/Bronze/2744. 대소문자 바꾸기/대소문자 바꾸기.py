n=input()
for i in n:
    if i.islower():
        i=i.upper()
    else:
        i=i.lower()
    print(i,end='')