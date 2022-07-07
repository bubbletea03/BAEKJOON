def sum_separated_digit(num):
    n1 = num%10 # 1의 자리
    n10 = (num-n1)/10 # 10의 자리 (num이 10 미만일 경우, 10의 자리는 0으로 처리됨.)
    return n1+n10

def get_1digit(num):
    return num%10


input_num = int(input());

new_num = input_num # 초기값
cycle = 0
while True:
    new_num = get_1digit(new_num)*10 + get_1digit(sum_separated_digit(new_num))
    cycle+=1
    if(new_num==input_num): # 입력했던 값으로 돌아올 경우
        break
print(cycle)

