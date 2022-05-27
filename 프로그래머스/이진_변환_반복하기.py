def solution(s):
    answer = []
    flag = True
    zero_count = 0
    cnt = 0
    temp = 0
    while flag:
        temp +=1
        if temp == 10 :
            flag = False
        first_s = len(s)
        s = s.replace("0", "")
        zero_count += first_s - len(s)

        s = bin(len(s))[2:]
        cnt +=1

        if s == "1":
            flag = False
    answer.append(cnt)
    answer.append(zero_count)

    return answer