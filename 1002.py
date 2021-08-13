n = int(input())

for i in range(n):
    x1, y1, r1, x2 ,y2, r2 = map(int, input().split())

    length = ((x2-x1)**2 + (y2-y1)**2)**(1/2)


    # 두 원이 완전히 겹칠 때 (length = 0) -> 교점 무한개
    if length == 0 and r1 == r2:
        print(-1)

    # 두 원이 내접하는 경우 
    elif length != 0 and (length == r2 - r1 or length == r1 - r2):
        print(1)

    # 두 원이 딱 한곳에서만 겹침 (length = r1 + r2) -> 교점 1개
    elif length == r1 + r2:
        print(1)

    # 두 원이 겹치지 않음 (length > r1 + r2) -> 교점 0개
    elif length > r1 + r2:
        print(0)

    # 두 원이 겹치지 않고 작은 원이 큰 원에 포함되어 있는 경우 -> 교점 0개
    elif length < r2 - r1 or length < r1 - r2:
        print(0)

    # 두 원이 두 곳에서 겹침
    else:
        print(2)