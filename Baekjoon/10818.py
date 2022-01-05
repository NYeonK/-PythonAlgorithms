N = int(input())

n = [0 for i in range(N)] # 입력받는 정수의 범위 지정

n = list(map(int, input().split()))

print(min(n), max(n))


