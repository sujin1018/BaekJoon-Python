def solution(record):
    answer = []
    dict={}
    for i in record:
        args=i.split()
        if args[0]!="Leave":
            dict[args[1]]=args[2]
    for i in record:
        args=i.split()
        if args[0]=="Enter":
            answer.append("%s님이 들어왔습니다." % dict[args[1]])
        elif args[0]=="Leave":
            answer.append("%s님이 나갔습니다." % dict[args[1]])
        else:
            continue
    return answer