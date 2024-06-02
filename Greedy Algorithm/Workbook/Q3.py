# 문자열 뒤집기

# 입력한 s값의 0,1 각 수를 헤아려 적은 수의 숫자를 뒤집기
s = input()

count0 = 0  # 전부 0으로 바꾸는 경우
count1 = 0  # 전부 1로 바꾸는 경우

if s[0] == '1':  # 입력한 값의 첫번째 숫자가 1인 경우
    count0 += 1  # 모두 0으로 바꾸는 경우의 수에 1추가
else:
    count1 += 1  #아니면 전부 1로 바꾸는 경우의 수에 1 추가

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i+1] == '1':
            count0 += 1
        else:
            count1 += 1