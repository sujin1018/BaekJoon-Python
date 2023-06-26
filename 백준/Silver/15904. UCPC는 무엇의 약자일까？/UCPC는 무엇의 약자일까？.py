a=input().replace(' ','')
b=['U','C','P','C']
x=0
for i in a:
    if i==b[x]:
        x+=1
    if x==4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")