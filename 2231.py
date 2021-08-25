inserted = input()

n = int(inserted)
numList = list(map(int, inserted))
loop = len(numList)

result = 10000001

for i in range(min(loop * 9, n)):
    # 테스트 케이스 만들기
    case = n - i - 1
    case_list = list(map(int, str(case)))
    
    sum = 0
    # 각 자리의 총합
    for j in range(len(case_list)):
        sum += case_list[j]

    if n == case + sum:
        result = min(result, case)

if result == 10000001:
    print("0")
else:
    print(result)