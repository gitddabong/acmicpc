import sys

n = int(sys.stdin.readline())

array = []
counting = [0] * 8001
sum = 0
for i in range(n):
    input = int(sys.stdin.readline())
    array.append(input)
    sum += input
    counting[input + 4000] += 1

# 최빈값 구하는 반복문
counting_max = -9999        # 빈도의 최댓값
max_index = 0               # 최빈값
for i in range(8001):
    if counting_max < counting[i]:
        counting_max = counting[i]
        max_index = i

mode = []
# 같은 최빈값이 있는 경우 서치
for i in range(8001):
    if counting[i] == counting_max:
        mode.append(i - 4000)
mode.sort()

#산술평균
sys.stdout.write(str(round(sum / n)) + '\n')

#중앙값
if n == 1:
    sys.stdout.write(str(array[0]) + '\n')
else:
    sorted_array = sorted(array)
    sys.stdout.write(str(sorted_array[int(n/2)]) + '\n')

#최빈값
if len(mode) == 1:
    sys.stdout.write(str(mode[0]) + '\n')
else:
    sys.stdout.write(str(mode[1]) + '\n')

#범위
sys.stdout.write(str(max(array) - min(array)) + '\n')
