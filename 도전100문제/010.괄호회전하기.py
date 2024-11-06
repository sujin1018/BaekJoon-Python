def solution(s):
  answer=0
  n=len(s)
  for i in range(n):
    stack=[]
    for j in range(n): # 문자열 회전
      c=s[(i+j)%n]
      if c=='(' or c=='[' or c=='{':
        stack.append(c)
      else:
        if not stack: # 짝이 맞지 않는 경우
          break
        # stack의 top과 짝이 맞는지 비교
        if c==')' and stack[-1]=='(':
          stack.pop()
        elif c==']' and stack[-1]=='[':
          stack.pop()
        elif c=='}' and stack[-1]=='{':
          stack.pop()
        else:
          break
    else: # for문이 break에 의해 끝나지 않고 끝까지 수행된 경우
      if not stack:
        answer+=1
  return answer