# 큰 수의 법칙
# 문제 - 주어진 수들을 M번 더하여 가장 큰 수를 만든다 특정 수가 연속 K번 초과해서 더할 수 없다
# 팁 - 입력값 중 가장 큰 수와 두번째로 큰 수만 저장

# ------------ 쉬운 풀이 ------------
n, m, k = map(int, input().split())  # 5 8 3
data = list(map(int, input().split()))  # 2 4 5 4 6 -> n=5 사용 완료

data.sort()  # 2 4 4 5 6 -> 작은 값 부터 오름차순
first = data[n - 1]  # 리스트 내 가장 마지막 값 aka 가장 큰 값
second = data[n - 2]  # 리스트 내 가장 마지막 바로 앞 값

result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += first
        m -= 1

    if m == 0:
        break

    result += second
    m -= 1
# 가장 큰 first 값을 result에 k번 더하기, 한번 더할때마다 m 1씩 차감 -> k번 다 더하면 second 값 한번 추가하고 m 한번 차감 -> m이 0이 될때까지 반복

print(result)

# ------------ 다른 풀이 ------------
n, m, k = map(int, input().split())
data = list(map(int, input.split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = int(m / (k + 1)) * k  # 가장 큰 수가 더해지는 횟수 계산ㄴ
count += m % (k + 1)

result = 0
result += (count) * first  # 가장 큰 수 더하기
result += (m - count) * second  # 두번째 큰 수 더하기

print(result)