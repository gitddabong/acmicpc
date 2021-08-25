n = int(input())
array = []
for i in range(n):
    weight, height = map(int, input().split())
    array.append((weight, height))

for i in array:
    count = 1
    for j in array:
        if i[0] != j[0] and i[1] != j[1]:
            if i[0] < j[0] and i[1] < j[1]:
                count += 1

    print(count, end=" ")
