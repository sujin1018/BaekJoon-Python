import sys
input=sys.stdin.readline
n=int(input())
a=input().split()
student={i:0 for i in a}
for _ in range(n):
    like=list(input().split())
    for i in like:
        student[i]+=1
student =sorted(student.items(),key=lambda x:(-x[1]))
for k,v in student:
    print(k,v)