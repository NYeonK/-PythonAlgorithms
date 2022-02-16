
s = input()
 
stack = []
multi = [] # 곱해줄 정수들
length = 0
point = ''


for str in s:

  # 문자열이 숫자일 경우
  if str.isdigit():
    point = str
    length += 1

  # 문자열이 '('일 경우
  elif str == '(':
    multi.append(point)
    stack.append(length-1)
    length = 0

  # 문자열이 ')'일 경우
  else:
    length = int(multi.pop()) * length + int(stack.pop())

print(length)
