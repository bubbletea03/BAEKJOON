def is_prime(num):
    for i in range(2, num):
        if(num%i==0):
            return False
    if(num>1):
        return True
    else:
        return False

n = int(input())
n_list = list(map(int, input().split()))
count = 0
for num in n_list:
    if(is_prime(num)):
        count += 1

print(count)
