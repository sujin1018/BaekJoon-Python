def solution(s):
  stack=[]
  for i in s:
    if stack and stack[-1]==i: # 스택이 비어있지 않고 현재 문자와 스택의 맨 위 문자가 같을 경우
      stack.pop()
    else:
      stack.append(i) # 스택에 현재 문자 추가
  return int(not stack) # 스택이 비어있으면 1, 비어있지 않으면 0