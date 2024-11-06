def solution(dirs):
  x,y=5,5
  ans=set() # 중복 제거
  for dir in dirs: # 다음 좌표 설정
    if dir=='U':
      dx,dy=x,y+1
    elif dir=='D':
      dx,dy=x,y-1
    elif dir=='L':
      dx,dy=x-1,y
    elif dir=='R':
      dx,dy=x+1,y
    if not (0<=dx<11 and 0<=dy<11): # 좌표평면 벗어날 경우
      continue
    # A -> B, B -> A 두 경우 추가(경로의 개수는 방향성이 없으므로)
    ans.add((x,y,dx,dy))
    ans.add((dx,dy,x,y))
    x,y=dx,dy # 좌표 업데이트
  return int(len(ans)/2) # 두 경우 추가했으므로 최종으로 2를 나눔