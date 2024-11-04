def solution(arr):
    arr=list(set(arr))
    arr.sort(reverse=True)
    return arr
