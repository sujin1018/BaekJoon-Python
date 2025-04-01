import sys
words = sys.stdin.read().splitlines()
for word in words:
    lower = sum(1 for i in word if i.islower())
    upper = sum(1 for i in word if i.isupper())
    digit = sum(1 for i in word if i.isdigit())
    space = sum(1 for i in word if i.isspace())
    print(f"{lower} {upper} {digit} {space}")