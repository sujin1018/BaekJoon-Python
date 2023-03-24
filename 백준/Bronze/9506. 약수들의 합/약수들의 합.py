import sys
input=sys.stdin.readline
while True:
    n=int(input())
    if n==-1:
        break
    a=[]
    for i in range(1,n):
        if(n%i==0):
            a.append(i)
    if(n==sum(a)):
        print(n,"="," + ".join(str(i) for i in a))
    else:
        print(n,"is NOT perfect.")
    
