def solution(decimal): # 스택으로 풀기
  stack=[]
  result=''
  while (decimal>0):
    stack.append(str(decimal%2))
    decimal//=2
  while stack:
    result+=stack.pop()
  return result

def solution2(decimal): # 슬라이싱
  stack=[]
  while (decimal>0):
    stack.append(str(decimal%2))
    decimal//=2
  return ''.join(stack[::-1])

def solution3(decimal): # 내장함수
  return bin(decimal)[2:]