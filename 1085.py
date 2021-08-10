x, y, w, h = map(int, input().split())

array = [w-x, h-y, x, y]

min = 10000
for i in range(4):
    if min > array[i]:
        min = array[i]

print(min)