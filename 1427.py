li = list(map(int, input()))

li.sort(reverse=True)
for i in range(len(li)):
    print(li[i], end='')