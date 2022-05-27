def solution(s):
    answer = 0

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(s)):
        for j in range(i, len(s)+1):
            if is_palindrome(s[i:j]):
                answer = max(answer, len(s[i:j]))
    return answer

def is_palindrome(s):
    length = len(s) // 2
    if len(s) % 2 == 1:
        if s[0:length] == s[length+1:][::-1]:
            return True
        return False
    else:
        if s[0:length] == s[length:][::-1]:
            return True
        return False
    return False