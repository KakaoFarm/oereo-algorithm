'''
해결과정 설명
1. 메인 함수가 도는 과정에서 total_card_cnt를 계산한 뒤 total_card_cnt가 0이 되는 조건에 종료
    - 현재의 커서가 있는 위치에 카드가 있을 경우
        - 엔터 함수 호출 (횟수 1 증가)
            - image_fair 라는 리스트가 있고 리스트안에 value가 2개가 있는지 없는지 체크
            - 2개 미만일 경우에는 리스트 안에 현재의 엔터가 호출된 카드의 좌표가 값을 저장
            - 2개 이상일 경우에는 리스트 안의 값들의 각 좌표값을 통해서 board 안의 카드 2장을 지우고 초기화
        - 엔터를 누른 현재의 커서위치의 카드에서 같은 모양의 카드를 찾음
            - 같은 모양의 카드가 있을 경우
                - 같은 x축 또는 y축에 있을 경우 ctrl + 커서에 해당하므로 횟수 1 증가
                - 같은 x축 또는 y축에 있지 않을 경우 횟수 2 증가
            - 같은 모양의 카드가 없을 경우 종료
    - 현재의 커서가 있는 위치에 카드가 없을 경우
        - x축 같은 선상에 있는 카드가 있는지 체크하고 그 카드를 하나 선택
        - y축 같은 선상에 있는 카드가 있는지 체크하고 그 카드를 하나 선택
        - 위의 2개 사항에 다 해당하지 않을 경우 bfs로 가장 가까이에 있는 카드를 하나 선택 -> 내 생각에는 이 경우가 문제가 있는 것 같음

    부르트 포스 정답
    모든 경우의 수를 확인

    ex)
    bfs -> 길 찾기 문제 -> 모든 경우의 수를 확인
    장점: 가장 가까운, 나쁜 길을 돌아가지 않음.

    빠른 방법
    느린 방법
    내가 구현하기 쉬운 방법으로 구현하기

    -> 1시간 컷....!!


'''

from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0


def solution(board, r, c):
    answer = 0
    image_pair = []
    total_card_cnt = 0

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != 0:
                total_card_cnt += 1

    answer = func(board, r, c, image_pair, total_card_cnt)
    print(answer)
    return answer


def func(board, r, c, image_pair, total_card_cnt):
    cnt = 0
    while True:
        if total_card_cnt <= 0:
            break
        if board[r][c] != 0:
            new_cnt, x, y, new_image_pair, total_card_cnt = enter(cnt, r, c, board[r][c], image_pair, board,
                                                                  total_card_cnt)

            image_pair = new_image_pair
            cnt = new_cnt
            new_x, new_y = detect_same_card(board, x, y)
            if total_card_cnt <= 0:
                break
            if new_x != -1 and new_y != -1:
                choose_x, choose_y, new_cnt = choose_direction(new_x, new_y, x, y, cnt)
                cnt = new_cnt
                r = choose_x
                c = choose_y
            if total_card_cnt <= 0:
                break
        else:
            if total_card_cnt <= 0:
                break
            new_cnt, new_x, new_y = detect_minimum_distance_card(board, r, c, cnt)
            r = new_x
            c = new_y
            cnt = new_cnt
    return cnt


def detect_minimum_distance_card(board, x, y, cnt):
    queue = deque()

    cnt = cnt
    for i in range(len(board)):
        if board[x][i] != 0:
            return cnt + 1, x, i
        if board[i][y] != 0:
            return cnt + 1, i, y

    queue.append((x, y))
    while queue:
        c_x, c_y = queue.popleft()

        for i in range(4):
            new_x = c_x + dx[i]
            new_y = c_y + dy[i]
            if new_y >= len(board) or new_x >= len(board) or new_x < 0 or new_y < 0:
                continue

            if board[new_x][new_y] != 0:
                return cnt + 2, new_x, new_y
            if board[new_x][new_y] == 0:
                queue.append((new_x, new_y))


def choose_direction(new_x, new_y, x, y, cnt):
    result_x = 0
    result_y = 0
    new_cnt = cnt

    if abs(new_x - x) < 1:
        new_cnt = new_cnt + 1
        result_x = x + (new_x - x)
        result_y = new_y
        return result_x, result_y, new_cnt
    if abs(new_y - y) < 1:
        new_cnt = new_cnt + 1
        result_y = y + (new_y - y)
        result_x = new_x
        return result_x, result_y, new_cnt
    if abs(new_x - x) >= 1:
        new_cnt = new_cnt + 1
        result_x = new_x
    if abs(new_y - y) >= 1:
        new_cnt = new_cnt + 1
        result_y = new_y
    return result_x, result_y, new_cnt


def detect_same_card(board, x, y):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == board[x][y] and i != x and j != y and board[i][j] != 0:
                return i, j
    return -1, -1


def enter(cnt, current_x, current_y, current_image_value, image_pair, board, total_card_cnt):
    if len(image_pair) < 2:
        image_pair.append([board[current_x][current_y], current_x, current_y])
    if len(image_pair) == 2:
        same_image(image_pair, board)
        total_card_cnt -= 2
        image_pair = []
    return cnt + 1, current_x, current_y, image_pair, total_card_cnt


def same_image(image_pair, board)
    if image_pair[0][0] == image_pair[1][0]:
        x_1 = image_pair[0][1]
        y_1 = image_pair[0][2]
        x_2 = image_pair[1][1]
        y_2 = image_pair[1][2]
        board[x_1][y_1] = 0
        board[x_2][y_2] = 0


solution(board, r, c)