def solution(keymap, targets):
    answer = []
    for target in targets:
        total = 0
        for i in target:
            flag = False
            t = 101
            for key in keymap:
                if i in key:
                    t = min(key.index(i) + 1, t)
                    flag = True
            if not flag:
                total = -1
                break
            total += t
        answer.append(total)
    return answer