def solution(id_list, report, k):
    answer = [0]*len(id_list)
    dict={i:0 for i in id_list}
    for i in set(report):
        args=i.split()
        dict[args[1]]+=1
    for i in set(report):
        args=i.split()
        if dict[args[1]] >= k:
            answer[id_list.index(args[0])]+=1
    return answer