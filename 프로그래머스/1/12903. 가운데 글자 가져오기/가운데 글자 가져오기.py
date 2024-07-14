def solution(s):
    length = len(s)//2
    return s[length] if len(s)%2==1 else s[length-1:length+1]