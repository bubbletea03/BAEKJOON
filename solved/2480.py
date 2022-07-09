# 같은 눈 몇 개인지 부터 확인
# 그 다음 IF문 쓰면 끝인 문제

num_list = list(map(int, input().split()))

for num in num_list: # 비교 기준점
    equal_count = num_list.count(num)
    if(equal_count > 1): # 숫자 3개밖에 없어서 2개만 같다 떠도 그게 최대이므로, 바로 탈출
        equal_num = num
        break

if(equal_count == 3):
    print(10000+equal_num*1000)
elif(equal_count == 2):
    print(1000+equal_num*100)
else:
    print(max(num_list)*100)