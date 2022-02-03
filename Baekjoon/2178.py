# bfs
# 1일때 이동 -> 전진하면서 +1로 바꿔줌

from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x,y))

  while queue: # 큐가 빌 때까지 반복
    x, y = queue.popleft()
    
    # 현재 위치에서 네 방향 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx<0 or ny <0 or nx>=n or ny >=m:
        continue
      if miro[nx][ny] == 0:
        continue
      if miro[nx][ny] == 1:
        miro[nx][ny] = miro[x][y] + 1
        queue.append((nx,ny))

  return miro[n-1][m-1]



n, m = map(int, input().split())

miro = []
for i in range(n):
  miro.append(list(map(int, input()))) 

# [상, 하, 좌, 우]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0,0))