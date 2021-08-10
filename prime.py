n, m = map(int, input().split())

i = n
while True:
    # 1 이하 숫자는 소수로 치지 않음
    if i <= 1:
        i += 1
        continue
    
    if i == m:
        break

    j = 2
    for j in range(i):
        if j == i:
            print(i)
            break

        # 나누어 떨어진다?
        if i % j == 0:
            break
        
        # 나누어 떨어지지 않는다
        else:
            continue

    i += 1