case1 = [3, 3, 6, 7, 7, 9]  # 12
case2 = [2, 2, 3, 3, 8, 8]  # 13
case3 = [5, 5, 5, 5, 5]   #6

def main():
    size = 0

    index = {}
    twin_sticks = []
    sole_sticks = []

    for case_number in case2:
        try:
            index[case_number] += 1
        except:
            index[case_number] = 1

    for key, value in index.items():
        if value//2 >=1:
            if value % 2 == 1:
                sole_sticks.append(key)
            for i in range(value//2):
                twin_sticks.append(key)
        else:
            sole_sticks.append(key)

    result = 0
    print(index)

    if len(sole_sticks) < len(twin_sticks) and len(twin_sticks) - len(sole_sticks) >=3:
        for i in range((len(twin_sticks) - len(sole_sticks))//3):
            print("sole: ", sole_sticks)
            print("twin: ", twin_sticks)
            sole_sticks.append(twin_sticks[i])
            sole_sticks.append(twin_sticks[i])
            del twin_sticks[i]

    print("sole: ", sole_sticks)
    print("twin: ", twin_sticks)

    for i in range(len(sole_sticks)):
        if len(twin_sticks) == 0:
            break
        result += twin_sticks[i] + 1
    print(twin_sticks)
    print(result)


main()