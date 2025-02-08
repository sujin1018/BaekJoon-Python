def solution(spell, dic):
    for i in dic:
        # 방법 1
        if sorted(spell) == sorted(list(i)):
        # 방법 2
        # if not set(spell) - set(i):
            return 1
    return 2
