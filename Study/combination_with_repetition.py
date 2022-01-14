# 중복조합 nHk = k+(n-1)Ck

# itertools 사용한 중복조합

from itertools import combinations_with_replacement

arr = [1,2,3]

for i in combinations_with_replacement(arr,3):
    print(i, end=" ")


#------------------------------------------

# 배와 감에 대해 중복을 허용하여 세 개 선택
# (배3), (배2,감1), (배1,감2), (감3)

# 5H3 = 7C3 = 35

n, k = 5,3
A = ['귤', '감', '배', '떡', '돈']
arr = [0]*k

def combi(level, start):
  #종료조건
  if level >= k:
    print(arr)
    return
  
  # lelvel마다 시작점은 다르지만, 끝점은 다 똑같다.
  # 그러므로 시작점은 받아오는 걸로 하고, 끝점은 데이터의 개수만큼이다.
  
  for i in range(start, len(A)):
    arr[level] = A[i]
    combi(level+1, i)

combi(0,0)

# 조합과 달리, 중복조합은 전에 선택된 것부터 시작점으로 선택할 수 있다.