list = []
sum=0

# 입력받아서 리스트 정렬
for i in range(0, 9):
  num = int(input())
  if num <= 100:
    list.append(num)
    sum +=num
list.sort()

sum = sum-100
exc = 0

# 두 난쟁이 찾아내기
while exc==0:
  for i in range(0,8):
    exc += list[i]
    for j in range(1,9):
      exc += list[j]

      if exc == sum: # 찾아냄
        del list[j]
        del list[i]
        for k in range(0, len(list)):
          print(list[k])
        exit()
        
      exc -= list[j]
    exc -= list[i]


