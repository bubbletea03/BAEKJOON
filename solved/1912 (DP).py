# 배열은 편의상 1부터 인덱스 시작
# dp[x] : x번째까지 최대한의 선택을 했을 때의 합
# 알고리즘 비교 방식: numbers[x]랑 dp[x-1] 중 더 큰 것을 dp[x]로 고름
# 연속이 "끊어지는 것"을 구현

n = int(input())

numbers = [0] + list(map(int, input().split()))
dp = [0] + [numbers[1]] + [0] * (n-1)

for i in range(2, n+1):
    dp[i] = max(numbers[i], dp[i-1]+numbers[i])

dp.pop(0)
print(max(dp))

# 소감:
# 일단 무조건 맞았다고 뜰 듯?
# 뭔가 와 닿지 않는 이유는, 규칙성을 찾다가 우연히 답을 떠올려냈기 때문인 듯.
# "dp[x] 에 최선의 답을 기록해나가면서, 깔끔하게 이용해먹으면서 나아가는 것"이 추론의 핵심이였다고 봄.
# 그렇게 생각하면, 기본 유형 문제 느낌