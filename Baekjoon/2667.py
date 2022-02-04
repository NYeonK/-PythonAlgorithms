# dfs
# (0.0)에서 시작해서 1이 보이면 그때부터 시작
# 단지 시작점부터 이동할 때, +1


def dfs(x,y):
  if x<0 or x>=n or y<0 or y>=n:
    return False

  if home[x][y]==1:
    global count
    count += 1
    home[x][y]=0

    dfs(x-1,y)
    dfs(x,y-1)
    dfs(x+1,y)
    dfs(x,y+1)

    return True

  return False


n = int(input())

home = []
danji = []

for i in range(n):
  home.append(list(map(int, input())))


total = 0
count = 0

for i in range(n):
  for j in range(n):

    if dfs(i,j)== True:
      total+=1
      danji.append(count)
      count = 0

print(total) # 단지 수

# 단지에 속하는 집의 수
danji.sort()
for i in range(len(danji)):
  print(danji[i])