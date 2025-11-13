def solution(brown, yellow):
    n=brown+yellow
    for b in range(1, int(n**0.5)+1):
        if n % b == 0:
            a = n // b
            if (a-2)*(b-2) == yellow:
                return [a,b]