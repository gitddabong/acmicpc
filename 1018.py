n,m  = map(int, input().split())

type_A = [
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"]
]

type_B = [
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"],
    ["B","W","B","W","B","W","B","W"],
    ["W","B","W","B","W","B","W","B"]
]

board = []
for i in range(n):
    board.append(list(map(str, input())))

result = 65
for i in range(n-8+1):
    for j in range(m-8+1):
        cnt_A = 0
        for x in range(8):
            for y in range(8):
                if board[x+i][y+j] != type_A[x][y]:
                    cnt_A += 1

        cnt_B = 0
        for x in range(8):
            for y in range(8):
                if board[x+i][y+j] == type_A[x][y]:
                    cnt_B += 1

        result = min(result, min(cnt_A, cnt_B))

print(result)