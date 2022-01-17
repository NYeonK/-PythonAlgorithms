# 중복순열 nπr

# itertools 사용한 중복순열

from itertools import product

arr=[1,2,3,4]
for i in product(arr,repeat=3):
    print(i, end=" ")


#------------------------------------------

# 재귀를 사용한 중복순열

n, r = 3,2
A = ['귤', '감', '배']
arr = [0]*r

def combi(level, start):
  #종료조건
  if level >= r:
    print(arr)
    return

  for i in range(len(A)):
    arr[level] = A[i]
    combi(level+1, i)

combi(0,0)