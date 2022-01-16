# 중복조합 nHk = k+(n-1)Ck

# itertools 사용한 중복조합

from itertools import combinations_with_replacement

arr = [1,2,3]

for i in combinations_with_replacement(arr,3):
    print(i, end=" ")


#------------------------------------------

# 재귀를 사용한 조합

n, k = 3,3
A = ['귤', '감', '배']
arr = [0]*k

def combi(level, start):
  #종료조건
  if level >= k:
    print(arr)
    return
  
  for i in range(start, len(A)):
    arr[level] = A[i]
    combi(level+1, i)

combi(0,0)
