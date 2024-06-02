# 모험가 길드

n = int(input())
data = list(map(int, input().split()))
data.sort()  # 1 2 2 2 3

result = 0 # 만들어질 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data:
    count += 1
    if count >= i:
        result += 1  # 현재 그룹에 포함된 모험가의 수(count)가 현재의 공포(i)도 이상이라면, 그룹 결성(result+=1)
        count = 0
# i=1 count=1 count>=i result=1 count=0 / i=2 count=1 count<i / i=2 count=2 count>=i result=2 count=0 / i=2 count=1 count<i / i=3 count=2 count<i

print(result)