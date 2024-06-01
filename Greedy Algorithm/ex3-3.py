# 숫자 카드 게임
# 문제 - 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는다
# 조건 - 카드는 n행*m열 형태, 행 선택 -> 그 중 가장 낮은 카드 뽑기
# 팁 - 각 행마다 가장 작은 수를 찾은 뒤에 그 수 중에서 가장 큰 수를 찾는다

# ------------ min()함수 사용 풀이 ------------
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))  # 행마다 숫자 입력, n행
    min_value = min(data)  # 입력한 행에서 가장 작은 값은 min_value에 저장
    result = max(result, min_value)  # min_value값과 최초 result값 0과 비교하여 큰 값을 result에 저장

print(result)

# ------------ 2중 반복문 구조 사용 풀이 ------------
n, m = map(int, input().split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)

    result = max(result, min_value)
print(result)