# 문자열 여러 차례에 걸쳐 입력 받은 후
# 탐색으로 a,e,i,o,u 생길 때마다 count 증가시키고 출력하고 끝

arr = []

while(True):
    sentence = input()
    if (sentence == '#'):
        break
    count = 0
    for char in sentence:
        if(char.lower() in ['a', 'e', 'i', 'o', 'u']):
            count += 1
    arr.append(count)

for num in arr:
    print(num)
