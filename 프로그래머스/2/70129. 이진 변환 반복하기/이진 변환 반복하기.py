def solution(s):
    zero, num = 0, 0
    while s != "1":
        cnt = len(s)
        s = s.replace("0",'')
        zero += cnt-len(s)
        s = bin(len(s))[2:]
        num += 1
    return [num, zero]