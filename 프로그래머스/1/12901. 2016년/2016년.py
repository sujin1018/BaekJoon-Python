def solution(a, b):
    days= ["THU","FRI","SAT","SUN","MON","TUE","WED"]
    months = [31,29,31,30,31,30, 31, 31, 30, 31, 30, 31]
    
    m = a - 1
    d = sum(months[:m]) + b
    return days[d%7]