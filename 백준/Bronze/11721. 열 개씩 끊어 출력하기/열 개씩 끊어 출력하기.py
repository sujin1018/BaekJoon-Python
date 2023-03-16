n=list(map(str,input()))
for i in range(1,len(n)+1):
    print(n[i-1],end='')
    if(i%10==0 and i!=0):
        print()
        
# 다른 풀이
n=input()
for i in range(0,len(n),10):
    print(n[i:i+10])
