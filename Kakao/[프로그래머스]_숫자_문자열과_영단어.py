def solution(s):
    answer = 0
    eng_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    temp = ""
    result = ""
    for char in s:
        temp += char
        if temp in eng_map.keys():
            result += str(eng_map[temp])
            temp = ""
        if temp.isdigit():
            result += temp
            temp = ""
    return int(result)
