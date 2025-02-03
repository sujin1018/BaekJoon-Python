def solution(n, arr1, arr2):
    answer = []
    # 방법 1
    arr1 = [bin(i)[2:].zfill(n) for i in arr1]
    arr2 = [bin(i)[2:].zfill(n) for i in arr2]
    for i in range(n):
        tmp = ''
        for j in range(n):
            if arr1[i][j]=='0' and arr2[i][j]=='0':
                tmp += ' '
            else:
                tmp += '#'
        answer.append(tmp)
        
    # 방법 2
    # for i in range(n):
    #     tmp = bin(arr1[i] | arr2[i])
    #     tmp = tmp[2:].zfill(n)
    #     tmp = tmp.replace('1','#').replace('0',' ')
    #     answer.append(tmp)
    return answer