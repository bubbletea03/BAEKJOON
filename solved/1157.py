# 기준점 잡고 돌면서 중복 횟수 잼
# 중복 횟수 가장 많은 알파벳이랑 횟수 기록
# max에 같은 알파벳이면 넘어가기, 더 높으면 덮어씌우는 식으로

# 사용된 알파벳이 무엇무엇이 있는지 반환
def getList_usedElements(list):
    result_list = []
    for e in list:
        if(e not in result_list):
            result_list.append(e)
    return result_list


char_list = list(input().upper())
max_count = 0
for char in getList_usedElements(char_list):
    char_count = char_list.count(char)
    if(char_count > max_count):
        max_count = char_count
        max_count_char = char
    elif(char_count == max_count):
        max_count_char = '?'

print(max_count_char)