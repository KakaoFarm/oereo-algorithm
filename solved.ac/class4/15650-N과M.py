n, m = map(int, input().split())

visited = [False] * (n)

def back_tracking(value):
    if value == m:
        if value == True in visited:
            print(visited.index(value)+1)
    else:
        for i in range(len(visited)):
            visited[i] = True
            back_tracking(value+1)
            visited[i] = False


back_tracking(0)