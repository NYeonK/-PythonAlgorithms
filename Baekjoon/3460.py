T = int(input()) 

while T>0:
  n = int(input("")) 
  list = []
  a = n/2
  b = n%2
  list.append(b)
  
  while a>0:
    if a>=2:
      b = a%2
      a = a/2
      b = int(b)
      list.append(b)
    else:
      a = int(a)
      list.append(a)
      break  

  # 1의 위치 반환
  result= [i for i, value in enumerate(list) if value == 1]
  for i in result:
    print(i, end=' ')
  
  T -= 1




# 정수 n을 2로 나눠줬는데, 실수로 표현돼서 해맸다. [1.0, 0.0, 0.0, 0]
# Python에서는 나눗셈 연산을 할 경우 항상 실수로 결과를 돌려준다. 
# 만약 정수를 원한다면 int로 형변환을 해줘야 함.




