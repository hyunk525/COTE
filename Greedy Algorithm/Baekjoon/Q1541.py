# 잃어버린 괄호
# 문제 - 괄호를 적절히 쳐서 이 식의 값을 최소로

# -가 앞으로오게, 합쳐진 큰 값을 뒤에서 뺀다 => - 기준으로 뒤에 괄호 추가

exp = input().split('-')  # '-'기준으로 split
num = []

for i in exp:
    sum = 0
    tmp = i.split('+')
    for j in tmp:
        sum += int(j)
    num. append(sum)
# '-'기준으로 split 된 값들을 더해서 추가할 리스트

n = num[0]

for i in range(1, len(num)):
    n -= num[i]

print(n)