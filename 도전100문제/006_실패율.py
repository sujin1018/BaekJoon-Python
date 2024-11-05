def solution(N,stages):
  user=[0]*(N+2) # 스테이지 도전자 수 초기화
  total=len(stages) # 스테이지 도달한 도전자 수
  fail={} # 실패율 저장할 딕셔너리
  for i in stages:
    user[i]+=1 # 스테이지별 도전자 수
  for i in range(1,N+1):
    if user[i]==0: # 도전자 없을 경우 실패율 0
      fail[i]=0
    else:
      fail[i]=user[i]/total # 실패율
      total-=user[i] # 다음 스테이지 실패율 위한 현재 스테이지 인원 빼기
  result=sorted(fail,key=lambda x: fail[x], reverse=True) # 내림차순 정렬
  return result