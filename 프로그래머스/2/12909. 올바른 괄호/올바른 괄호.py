def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                return False
            if stack[-1] == '(':
                stack.pop()
    if stack:
        return False
    return True