
# DFS 선언
def dfs(v): 
  visited[v] = True # 방문 체크
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


# 입력: 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
#       다음 M개의 줄에는 간선이 연결하는 두 정점의 번호 (입력으로 주어지는 간선은 양방향)
import sys

n, m, v = map(int, sys.stdin.readline().split())
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False] * (n + 1)


for _ in range(m): 
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = graph[b][a] = 1


dfs(v)
print() 
bfs(v)