# ATM
# 문제 - n명, 각 사람이 돈을 인출하는데에 걸리는 시간 Pi, 전체 시간 합의 최솟값

# 가장 작은값부터 정렬하고 더하기
n = int(input())
pertimelist = list(map(int, input().split()))

pertimelist.sort()

totaltime = 0

for i in range(1, n+1):
    totaltime += sum(pertimelist[0:i])

print(totaltime)