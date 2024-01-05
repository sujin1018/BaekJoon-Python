import sys
a=sys.stdin.read()
s=[0]*26
for i in a:
    if i.islower():
        s[ord(i)-97]+=1
for i in range(26):
    if s[i]==max(s):
        print(chr(97+i),end='')