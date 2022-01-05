
train = 0
list = []

for i in range(0,10):
  off, on = map(int, input().split()) # 내린 사람, 탄 사람 차례대로 입력 받기
  train = (train - off) + on
  list.append(train)

print(max(list))
