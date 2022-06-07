def solution(participant, completion):
    answer = ''
    participants = dict()
    completions = dict()

    for value in participant:
        if value not in participants:
            participants[value] = 1
        else:
            participants[value] += 1

    for value in completion:
        if value in participants:
            participants[value] -= 1

    for index, value in participants.items():
        if value != 0:
            answer = index

    return answer