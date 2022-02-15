# 압축이 풀린 문자열 S의 길이 출력
# 부분 문자열 K(Q) : K는 한자리 정수, Q는 0이상의 문자열


# 입력받은 후, 문자열 종류에 따라 구분
# '('면 그 앞까지 stack에 넣어두기
# 바로 앞 숫자를 따로 multi 변수에 저장,
#  ')'면 괄호 안에 있는 길이를 카운트해서 곱하기 multi 하기

s = input()

stack = []
length = 0
point = ''


for str in s:

  # 문자열이 숫자일 경우
  if str.isdigit():
    point = str
    length += 1

  # 문자열이 '('일 경우
  elif str == '(':
    length -= 1
    point - 1 

  # 문자열이 ')'일 경우
  else:
    print()

print(length)

# str.isdigit()

# 문자열이 '숫자'로만 이루어져있는지 확인하는 함수 입니다.

# 문자가 '단 하나'라도 있다면 False를 반환하고,
# 모든 문자가 '숫자'로만 이루어져있으면 True를 반환합니다.

# 사용법
# 1) str.isdigit("판단하고자 하는 문자열")
# 2) "판단하고자 하는 문자열".isdigit()
