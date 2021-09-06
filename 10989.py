import sys

n = int(sys.stdin.readline())       # 자바 식 입력

li = [0] * 10001
for i in range(n):
    li[int(sys.stdin.readline())] += 1

for i in range(10001):
    if li[i] == 0:
        continue
    
    for j in range(li[i]):
        sys.stdout.write(str(i) + '\n')