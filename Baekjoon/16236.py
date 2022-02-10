# 상하좌우의 물고기들의 크기를 확인해가며 전진하고
# 이동 거리의 최솟값을 구해야하기 때문에 bfs

from collections import deque

def bfs(x, y):
  BabyShark = 2
  global space
  count = 0
  fish = 0

  queue = deque()
  queue.append((x,y))
  
  while queue: # 큐가 빌 때까지 반복
    x, y = queue.popleft()
    visited[x][y] = 1
    
    # 현재 위치에서 네 방향 확인
    for i in range(4):
      nx = x + dx[i] #좌우 
      ny = y + dy[i] #상하
      #print(x,y)

      if nx>=n or ny >=n or nx<0 or ny<0:
        continue
      if space[nx][ny] > BabyShark:
        continue
      if space[nx][ny] <= BabyShark and visited[nx][ny] == 0:
        # space[nx][ny] = space[x][y] + 1
        count += 1

        if space[nx][ny] < BabyShark:
          fish += 1
          space[nx][ny] = 0
          if fish == BabyShark:
            BabyShark += 1

        queue.append((nx,ny))
        #if space[nx][ny] == 0:
        #  continue


  #return space[n-1][n-1]
  print(BabyShark)
  return count


n = int(input())

space = []
visited = [[0 for col in range(n)] for row in range(n)]

for i in range(n):
  space.append(list(map(int, input().split()))) 

# [좌, 우, 상, 하]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
  for j in range(n):
    if space[i][j] == 9:
      print(bfs(i,j))
