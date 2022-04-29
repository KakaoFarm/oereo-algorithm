def solution(id_list, report, k):
    answer = []
    support_users = dict()
    supported_users = dict()

    for user_id in id_list:
        support_users[user_id] = []
        supported_users[user_id] = []

    report = set(report)

    for report_value in report:
        support_user, supported_user = report_value.split()
        support_users[support_user].append(supported_user)
        supported_users[supported_user].append(support_user)

    for index, value in support_users.items():
        temp = 0
        for user in value:
            if len(supported_users[user]) >= k:
                temp += 1
        answer.append(temp)

    return answer
