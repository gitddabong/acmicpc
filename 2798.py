n, m = map(int, input().split())
array = list(map(int, input().split()))

result = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = array[i] + array[j] + array[k]
            if sum <= m:
                result = max(result, sum)
                
print(result)