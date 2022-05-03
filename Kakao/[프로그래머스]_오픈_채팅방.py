def solution(record):
    user_uid = dict()
    answer = []
    # print(record)
    for info in record:
        data = info.split()
        if data[0] == "Enter":
            if data[1] not in user_uid:
                user_uid[data[1]] = data[2]
                answer.append(f'{data[1]}님이 들어왔습니다.')
            else:
                user_uid[data[1]] = data[2]
                answer.append(f'{data[1]}님이 들어왔습니다.')
        if data[0] == "Leave":
            answer.append(f'{data[1]}님이 나갔습니다.')
        if data[0] == "Change":
            user_uid[data[1]] = data[2]

    temp = []
    for value in answer:
        user_id = value.split("님")[0]
        new_value = value.replace(user_id, user_uid[user_id])
        temp.append(new_value)

    return temp