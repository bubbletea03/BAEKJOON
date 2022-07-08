# DP

# 규칙 - 숫자가 3 위로 뜰 경우 그 분기로 분리해서 경우의 수를 따질 수 있다. (분리한 후 마지막에 곱한다)
# dp[x]에다가 연속 숫자 기준 x자리 숫자의 경우의 수를 담는다.

# ex) 
# dp[2]: 11 = 2 
# dp[3]: 111 = 3 
# dp[4]: 1111 = 5
# dp[5]: 11111 = 8

# 풀이법
# 일단 1 1 1 1 1 에서 +1
# 11 1 1 1 에서 오른쪽 남은 개수 3개이므로 +dp[3]
# 1 11 1 1 에서 오른쪽 남은 개수 2개이므로 +dp[2]
# 1 1 11 1
# 1 1 1 11 하고 마무리

# 행은 n-1개
# 11 1 1 1
# 1 11 1 1
# 1 1 11 1
# 1 1 1 11




def func(n):

    # 편의상 인덱스 1부터 시작, 기본값 1
    dp = [1] * (n+1)
    dp[2] = 2
    if(n>2):
        dp[3] = 3

    for i in range(4, n+1):
        for row in range(1, n):
            if(row >= i-2):
                dp[i] += 1
            else:
                dp[i] += dp[i-1-row]

    return dp[n]



nlist = list(str(input()))

dpS = []
i = 0
j = 0
for num in nlist:
    j += 1
    if(int(num) > 2 or i == len(nlist)-1):
        dpS.append(func(j))
        j = 0
    i += 1

print(dpS)



