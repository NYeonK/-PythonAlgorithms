# 조합 nCk

# itertools 사용한 조합

from itertools import combinations

arr = [1,2,3,4,5]
for i in combinations(arr,3):
  print(i, end='')

# ------------------------------------------------

# 조합의 수 구하기

def combination(n,k):
  if k==0:
    return 1
  elif n<k:
    return 0
  else:
    return combination(n-1,k-1)+combination(n-1,k)

print(combination(5,3))

# --------------------------------------------------

# 반복문을 사용한 조합

A = [1,2,3,4,5]

def func(n):
  for i in range(n-2):
    for j in range(i+1, n-1):
      for k in range(j+1, n): # i+2부터 범위를 잡게되면, 동일한 숫자가 포함될 수 있다.
        print(A[i], A[j], A[k])

func(len(A))

#---------------------------------------------------

# 재귀를 사용한 조합

n=5
k=3
arr = [0]*k
A=[1,2,3,4,5]

def combi(level, S):
  # 종료조건
  if level >= k:
    print(arr)
    return

# S : 시작점              
  for i in range(S, n-k+level+1): # range를 사용하므로 +1   
    arr[level] = A[i]
    combi(level+1, i+1) # 다음 시작점(S)는 지금 숫자의 다음부터 진행해야 하므로 i+1

combi(0,0)