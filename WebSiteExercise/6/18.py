def in_that_regions(grid, elem_x, elem_y):
    x = (elem_x)//3*3
    y = (elem_y)//3*3
    area = []

    for i in range(x, x+3):
        for j in range(y, y+3):
            area.append(grid[i][j])

    return area


def naked_single(grid):
    has_done_something = True

    while has_done_something:
        has_done_something = False
        for x in range(9):
            for y in range(9):
                if grid[x][y] != 0:
                    continue

                tmp = set(grid[x])
                tmp.update(grid[i][y] for i in range(9))
                tmp.update(in_that_regions(grid, x, y))

                tmp = set((1,2,3,4,5,6,7,8,9)) - tmp

                if len(tmp) == 1:
                    grid[x][y] = tmp.pop()
                    has_done_something = True
                elif not(tmp):
                    return False, None


    for i in range(9):
        if 0 in grid[i]:
            return False, None

    return True, grid
