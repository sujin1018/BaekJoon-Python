count=0
for _ in range(int(input())):
    stack = []
    word = input()
    for i in word:
        if stack and i==stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    if not stack:
        count+=1
print(count)