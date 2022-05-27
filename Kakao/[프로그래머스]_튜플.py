def solution(s):
    answer = []

    splited_data = s[2:len(s)-2].split("},{")
    splited_data.sort(key=lambda value: len(value))

    for data in splited_data:
        splited = data.split(",")
        for value in splited:
            if int(value) not in answer:
                answer.append(int(value))
    return answer