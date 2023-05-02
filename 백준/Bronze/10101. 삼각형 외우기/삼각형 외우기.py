s=[int(input()) for _ in range(3)]
if s.count(60)==3:
    print('Equilateral')
elif sum(s)==180 and len(set(s))==2:
    print('Isosceles')
elif sum(s)==180 and len(set(s))==3:
    print('Scalene')
else:
    print('Error')