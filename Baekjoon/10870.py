n = int(input())

def fibonacci(n):
  if n==1 or n ==0:
    return n
  elif n>20:
    exit()
  else:
    return fibonacci(n-2) + fibonacci(n-1) #재귀

fibo = fibonacci(n)

print(fibo)