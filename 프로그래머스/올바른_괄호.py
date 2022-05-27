def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    cnt = 0
    for value in s:
        if value == "(":
            cnt +=1
        if value == ")" and cnt >0:
            cnt -=1
    # print(cnt)
    if cnt == 0 and s[0] != ")":
        return True
    elif cnt != 0 or s[0] == ")":
        return False