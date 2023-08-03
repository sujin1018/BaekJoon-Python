res=''
for i in input():
    if i.isupper():
        x=ord(i)+13
        if x>90:
            x-=26
        res+=chr(x)
    elif i.islower():
        x=ord(i)+13
        if x>122:
            x-=26
        res+=chr(x)
    else:
        res+=i
print(res)