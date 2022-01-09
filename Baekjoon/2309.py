list = []

for i in range(0, 9):
  num = int(input())
  if num <= 100:
    list.append(num)
list.sort()

print(list)

sum=0

while sum<100:
  for i in range(0, 8):
    list.remove(i)
    for j in range(0,8):
      list.remove(j)
      for k in range(0,7):
        sum += list[k]

print(sum)        
    


