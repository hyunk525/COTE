# 1이 될 때까지
# 문제 - n이 1이 될 때까지 n에서 1을 뺀다/ n을 k로 나눈다 과정 중 하나를 반복적으로 선택하여 수행한다 최소 실행 횟수
# 팁 - k로 최대한 많이 나눌 수 있도록 한다

# ------------ 쉬운 풀이 ------------
n, k = map(int, input().split())
result = 0

while n >= k :
    while n & k != 0:
        n -= 1
        result += 1
    n //= k
    result += 1

while n > 1:
    n -= 1
    result += 1

print(result)

# ------------ 다른 풀이 ------------
n, k = map(int, input().split())
result = 0

while True:
    target = (n // k) * k
    result += (n-target)
    n=target

    if n < k:
        break
    result += 1
    n //= k

result += (n-1)
print(result)