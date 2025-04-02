import sys
input = sys.stdin.readline

for _ in range(int(input())):
    t = input().strip()

    num = '0' if '0' in t else '1'
    left = t.split(num)[0].count('!')
    right = t.split(num)[1].count('!')

    if right > 0:
        num = '1'
    if left % 2 == 1:
        num = '0' if num == '1' else '1'
    print(num)