import math
n = int(input())

array = [[" "]*n for _ in range(n)]
rout_n = int(n**(1/3))


def fill_star(size, x, y):
    if size == 1:
        array[y][x] = '*'

    else:
        next_size = size // 3

        fill_star(next_size, x + 0*next_size, y + 0*next_size)  
        fill_star(next_size, x + 0*next_size, y + 1*next_size)  
        fill_star(next_size, x + 0*next_size, y + 2*next_size)  

        fill_star(next_size, x + 1*next_size, y + 0*next_size)  
        fill_star(next_size, x + 1*next_size, y + 2*next_size)  

        fill_star(next_size, x + 2*next_size, y + 0*next_size)  
        fill_star(next_size, x + 2*next_size, y + 1*next_size)  
        fill_star(next_size, x + 2*next_size, y + 2*next_size)  
"""
        for dy in range(3):
            for dx in range(3):
                if dy != 1 or dx != 1:
                    fill_star(next_size, x + dx*next_size, y + dy*next_size)
"""
fill_star(n, 0, 0)

for i in range(n):
    for j in range(n):
        print(array[i][j], end="")
    print()
