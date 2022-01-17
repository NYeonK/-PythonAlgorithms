# 순열 nPr

# itertools 사용한 순열

from itertools import permutations

arr=[1,2,3,4,5]

print(list(permutations(arr,3)))
print(len(list(permutations(arr,3)))) #개수

#--------------------------------------------

# 반복문을 사용한 순열

for i in range(1,4):
    for j in range(1,4):
        if i==j: continue
        for k in range(1,4):
            if i==k or j==k: continue
            print(i,j,k)


# visited[]를 이용한 반복문

visited = [0]*4 
arr = [0]*3     # list 형태로 출력하고 싶을 때

for i in range(1,4):
    visited[i] = 1      # arr[0] = i
    
    for j in range(1,4):
        if visited[j]: continue
        visited[j]=1        # arr[1] = j
       
        for k in range(1,4):
            if visited[k]: continue
            visited[k]=1        # arr[2] = k
           
            print(i,j,k)        # print(arr)
           
    # 사용해제
            visited[k]=0        # arr[2] = 0
        visited[j]=0        # arr[1] = 0
    visited[i]=0        # arr[0] = 0


#--------------------------------------------


# 재귀를 사용한 순열

A = [1, 2, 3, 4]
N = len(A)  
visited = [0]*N 
arr = [0] * N  
arr_list = [] 

def permutation(level):

    # 종료조건
    if level >=N: 
        #print(arr)
        arr_list.append(arr.copy())
        return

    for i in range(N):
        if visited[i]:continue
        visited[i] = 1
        arr[level] = A[i]
        permutation(level+1) 
        arr[level] = 0 
        visited[i] = 0 


permutation(0)
print(arr_list)
