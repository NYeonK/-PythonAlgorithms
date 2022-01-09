# nCk

# from itertools import combinations

# arr = [1,2,3,4,5]
# for i in combinations(arr,3):
#   print(i, end='')

# ------------------------------------------------

# 조합의 수 구하기
# def combination(n,k):
#   if k==0:
#     return 1
#   elif n<k:
#     return 0
#   else:
#     return combination(n-1,k-1)+combination(n-1,k)
# 
# combination(5,3)

# --------------------------------------------------

def combination(arr,k):
  result = []

  if len(arr)==k:
    return arr
  elif len(arr)<k or k==0:
    return []
  else:
    for i in range(0, len(arr)):
      center = arr[i]
      next_arr = arr[i+1:]
      
      for j in combination(next_arr, k-1):
        result.append([center]+j)
        #k=0이 되는 순간,,이 옴

    return result


arr = [1,2,3,4,5]
print(combination(arr,3))
# TypeError: 'int' object is not iterable

