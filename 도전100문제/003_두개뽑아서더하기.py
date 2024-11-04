def solution(arr):
    result=[]
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            result.append(arr[i]+arr[j])
    return sorted(set(result))
