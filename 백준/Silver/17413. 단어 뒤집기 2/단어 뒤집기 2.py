a=list(input())
f=False
res,stack="",""
for i in a:
    if f==False:
        if i=="<":
            f=True
            stack+=i
        elif i==" ":
            stack+=i
            res+=stack
            stack=""
        else:
            stack=i+stack
    else:
        stack+=i
        if i==">":
            f=False
            res+=stack
            stack=""
print(res+stack) 