def solution(nums):
    n=len(nums)//2
    nums=set(nums)
    answer = min(n,len(nums))
    return answer