def solution(prices):
  n=len(prices)
  answer=[0]*n # 가격이 떨어지지 않은 기간
  stack=[0] # 인덱스가 들어감
  j=0
  for i in range(1,n):
    while stack and prices[i] < prices[stack[-1]]: 
      # 가격이 떨어졌을 경우
      j=stack.pop()
      answer[j]=i-j # 가격이 떨어지지 않은 기간
    stack.append(i)
  # 가격이 떨어지지 않은 경우
  while stack:
    j=stack.pop()
    answer[j]=n-1-j
  return answer