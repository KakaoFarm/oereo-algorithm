def solution(N, stages):
    temp = {0: 0}
    temp_list = []
    result = {}
    answer = []

    for i in range(N):
        result[i + 1] = 0
        temp[i + 1] = 0

    for stage in stages:
        if stage not in temp:
            temp[stage] = 1
        else:
            temp[stage] += 1

    flag = len(stages)
    for i in range(N):  # 0,1,2,3
        if i in temp and i + 1 in temp:
            flag = flag - temp[i]
            # print("flag: ", flag)
            # print("temp[i+1]: ", temp[i+1])
            if temp[i + 1] == 0:
                result[i + 1] = 0
            else:
                result[i + 1] = temp[i + 1] / flag

    sorted_result = sorted(result.items(), key=lambda item: item[1], reverse=True)
    for value in sorted_result:
        answer.append(value[0])
    return answer
