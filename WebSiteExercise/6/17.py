def check_rows(grid):
    for i in grid:
        i.sort()
        if i != [1,2,3,4,5,6,7,8,9]:
            return False
    return True

def check_cols(grid):
    for i in range(9):
        tmp = [j[i] for j in grid]
        tmp.sort()
        if tmp != [1,2,3,4,5,6,7,8,9]:
            return False
    return True

def check_regions(grid):
    for i in range(3):
        for j in range(3):
            tmp = []
            for x in range(i*3, i*3+3):
                for y in range(j*3, j*3+3):
                    tmp.append(grid[x][y])

            tmp.sort()
            if tmp != [1,2,3,4,5,6,7,8,9]:
                return False
    return True

def check_sudoku(grid):
    return check_cols(grid) and check_regions(grid) and check_rows(grid)
