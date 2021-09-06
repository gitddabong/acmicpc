import sys

n = int(sys.stdin.readline())       # 자바 식 입력

array = [0] * n
for i in range(n):
    array[i] = int(sys.stdin.readline())

for i in sorted(array):
    sys.stdout.write(str(i) + '\n')     # 자바 식 출력