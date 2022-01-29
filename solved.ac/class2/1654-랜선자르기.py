# silver 3
import sys

def main():
    lan_cables, target_lan_cable_count = inputer()
    max_lan_cable_length = get_max_lan_cable_length(lan_cables, target_lan_cable_count)
    return max_lan_cable_length


# def get_max_lan_cable_length(lan_cables, target_lan_cable_count):
#     flag = 1
#     lan_cable_split_count = 2 ** 31
#     index = 0
#
#     while lan_cable_split_count >= target_lan_cable_count:
#         lan_cable_split_count = 0
#         for lan_cable in lan_cables:
#             lan_cable_split_count += lan_cable // flag
#
#         flag = flag + 1
#         index += 1
#     return index -1

def get_max_lan_cable_length(lan_cables, target_lan_cable_count):

    left, right = 1, max(lan_cables)
    result = 0

    while left <= right:
        lan_cable_split_count = 0
        mid = (left + right) // 2
        for lan_cable in lan_cables:
            lan_cable_split_count += lan_cable // mid

        if lan_cable_split_count >= target_lan_cable_count:
            left = mid + 1
            result = mid
        else:
            right = mid-1
    return result


def inputer():
    lan_cable_information = list(map(int, input().split()))
    lan_cables = list()
    for i in range(lan_cable_information[0]):
        data = sys.stdin.readline().rstrip()
        lan_cables.append(int(data))
    return lan_cables, lan_cable_information[1]


print(main())
