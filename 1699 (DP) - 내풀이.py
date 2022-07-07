# N => 1^2 * N 형태를 만듬
# N => 1^2*? + X^2*?
# N => 1^2*? + (X-1)^2*? + X^2*?
# N => 1^2*? + (X-2)^2*? + (X-1)^2*? + X^2*?
# ...
# 이렇게 점점 채우는 방식으로 풀면 될 듯
# X^2는 N안에 들어갈 수 있는 최대한의 제곱수를 의미함.

# squareNumbers[i] 에다가 <i번째 제곱수의 개수> 담고, 배열 다 더해서 총 항 개수 출력하면 될 듯.

# 1단계: 먼저 X를 구해야 함.
# 2단계: X로 채우고, X-1로 채우고, X-2로 채우고 ... 2^2로 채우고
# 3단계: 전부 수행 후 제곱수의 개수 저장해둔 squareNumbers[i]를 다 더하면 답임.

N = int(input())

# 1단계
for i in range(1, N+1):
    if(N >= i**2):
        X = i
    else:
        break

# 배열 생성.
# 1번째 칸부터 사용할 것이므로 배열 크기는 (X+1)
squareNumbers = [0] * (X+1)

# 1^2는 N개로 시작
squareNumbers[1] = N

# 2단계
for i in range(X, 1, -1):
    # 들어가는 만큼 넣음
    while(squareNumbers[1]-i**2 >= 0):
        squareNumbers[1] -= i**2
        squareNumbers[i] += 1

# 3단계
count_sum = 0
for i in range(1, X+1):
    print(f"{i} : {squareNumbers[i]}개")
    count_sum += squareNumbers[i]

print(count_sum)
