score,res=0,0
for _ in range(10):
    score+=int(input())
    if 100-res >=abs(100-score):
        res=score
print(res)