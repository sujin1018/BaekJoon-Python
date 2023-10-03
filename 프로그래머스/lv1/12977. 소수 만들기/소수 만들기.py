from itertools import combinations
def prime(x):
    if x<=1:
        return False
    else:
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return False
        return True
def solution(nums):
    answer=0
    a=list(combinations(nums,3))
    for i in a:
        if prime(sum(i)):
            answer+=1
    return answer
