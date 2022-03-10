import sys

N = int(input())

online_judge_map = list()
for i in range(N):
    member_information_map = list()
    member_information = list(map(str, input().split()))
    member_information_map.append(int(member_information[0]))
    member_information_map.append(member_information[1])
    member_information_map.append(i)
    online_judge_map.append(member_information_map)


online_judge_map.sort(key=lambda x: (x[0], x[2]))


for member_information in online_judge_map:
    print(member_information[0], member_information[1])
