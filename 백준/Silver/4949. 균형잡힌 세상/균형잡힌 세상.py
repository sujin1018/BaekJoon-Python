while True:
    n=input()
    s=[]
    if n=='.':
        break
    for i in n:
        if i=='[' or i=='(':
            s.append(i)
        elif i==']':
            if len(s)!=0 and s[-1]=='[':
                s.pop()
            else:
                s.append(']')
                break
        elif i==')':
            if len(s)!=0 and s[-1]=='(':
                s.pop()
            else:
                s.append(')')
                break
    if len(s)==0:
        print('yes')
    else:
        print('no')