import sys
input=sys.stdin.readline
for i in range(int(input())):
    a=list(map(int,input().split()))
    s=sorted(a[1:])
    diff=0
    for j in range(len(s)-1):
        diff=max(diff,s[j+1]-s[j])
    print("Class", i+1)
    print(f"Max {s[-1]}, Min {s[0]}, Largest gap {diff}")