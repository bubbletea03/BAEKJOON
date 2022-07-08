# 마지막 줄은 따로 출력. 마지막 줄은 따로 규칙이 있음

n = int(input())

for i in range(0, n-1): # 행

    # 별 나오기 전의 공백
    print(" " * (n-i-1), end="")
    print("*", end="")

    # 1층은 별 또 출력하는거 해당 X
    if(i>0):
        # 별 나온 후의 공백
        print(" " * (2*i-1), end="")
        print("*", end="")

    print("")

print("*" * (2*n-1), end="")