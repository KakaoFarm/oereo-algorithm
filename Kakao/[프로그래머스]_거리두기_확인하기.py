from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def solution(places):
    answer = []
    place_dict = dict()
    for i in range(len(places)):
        for j in range(len(places[0])):
            for k in range(len(places[0])):
                if places[i][j][k] == "P":
                    temp_map = places[i]
                    visited_map = [[-1] * len(places[0]) for _ in range(len(places[0]))]
                    flag = bfs(temp_map, j, k, visited_map)
                    if flag:
                        place_dict[i] = True
    
    for i in range(len(places)):
        if i in place_dict:
            answer.append(0)
        else:
            answer.append(1)
    return answer

def bfs(temp_map, i, j, visited_map):
    queue = deque()
    queue.append((i, j))
    visited_map[i][j] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=5 or ny>=5: continue
            
            if temp_map[nx][ny] != "X" and visited_map[nx][ny] == -1:
                if (temp_map[nx][ny] == "P" and visited_map[x][y] == 1) or (temp_map[nx][ny] == "P" and visited_map[x][y] == 0):

                    return True
                visited_map[nx][ny] = visited_map[x][y] + 1
                queue.append((nx, ny))
    
    return False
            