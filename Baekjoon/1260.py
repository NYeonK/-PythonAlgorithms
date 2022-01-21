
# DFS 선언
def dfs(v): 
  visited[v] = True
  print(v, end=' ')
  for i in range(1, n+1):
    if not visited[i] and graph[v][i] == 1:
      dfs(i)



# BFS 선언
from collections import deque

def bfs(v): 
  queue = deque([v])
  visited[v] = False 
  
  while queue: 
    v = queue.popleft() 
    print(v, end=" ") 
    for i in range(1, n+1): 
      if visited[i] and graph[v][i] == 1: 
        queue.append(i) 
        visited[i] = False



import sys

n, m, v = map(int, sys.stdin.readline().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False] * (n + 1)

# graph = [[0 0 0 0 0],[0 0 0 0 0],[0 0 0 0 0],[0 0 0 0 0],[0 0 0 0 0]]
# visited = [False False False False False]


for _ in range(m): 
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1

# graph = [[0 0 0 0 0],[0 0 1 1 1],[0 1 0 0 1],[0 1 0 0 1],[0 1 1 1 0]]

dfs(v)
print() 
bfs(v)