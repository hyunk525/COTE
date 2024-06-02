# 동전 0
# 문제 - 동전 n종류, n개, 합 K => 필요한 최소 동전 개수

n, k = map(int, input().split())
cointypes = list(int(input().split('/n')))

cointypes.sort()

count = 0

for coin in cointypes:
    count += n // coin
    n %= coin

print(count)

# ----------------------------
N, K = map(int, input().split())
coin_lst = list()
for i in range(N):
    coin_lst.append(int(input()))

count = 0
for i in reversed(range(N)):
    count += K//coin_lst[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K%coin_lst[i] # K는 동전으로 나눈 나머지로 계속 반복

print(count)
# ----------------------------
# 1. 계산대 안에 있는 돈의 수와 거슬러 줄 돈을 구합니다.
N, K = map(int, input().split()) # N : 화폐 종류수, K : 거슬러 줄 돈

# 2. 계산대에 있는 화폐들을 리스트의 형태로 입력받습니다.
coins = []
for _ in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)
# coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]

# 3. 만약 '계산대 안에 있는 화폐'보다 '거슬러 줄 돈'이 크다면
# 돈을 거슬러 줍니다.
answer = 0
for coin in coins:
    if K >= coin:  # K를 나눌 수 있는 가장 큰 수 찾기
        answer += K // coin # K를 coin으로 나누고 answer에 몫만큼 더하기
        K %= coin # 나머지는 k에 할당
        if K <= 0: # 만약 K가 0이면 반복문을 탈출합니다.
       		break
print(answer) # 거슬러 준 동전 + 화폐의 수