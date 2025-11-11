import math

def solution(progresses, speeds):
    left = []
    answer = []
    for i in range(len(progresses)):
        left.append(math.ceil((100 - progresses[i]) / speeds[i]))
        
    pivot, count = left[0], 0
    for i in left:
        if i <= pivot:
            count += 1
        else:
            answer.append(count)
            count = 1
            pivot = i
    answer.append(count)
    return answer