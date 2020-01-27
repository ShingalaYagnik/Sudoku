def isSafe(grid, row, col, i):
    return not Inrow(grid, row, col, i) and not Incol(grid, row, col, i) and not InBox(grid, row, col, i)


def Inrow(grid, row, col, i):
    # print("Inrow")
    for cols in range(9):
        if grid[row][cols]==i:
            # print("Inrow true")
            return True
    return False


def Incol(grid, row, col, i):
    # print("Incol")
    for rows in range(9):
        if(grid[rows][col]==i):
            # print("Incol true")
            return True
    return False


def InBox(grid, row, col, i):
    # print("Inbox")
    x = row-row%3
    y = col-col%3
    # print(x, y," ha ")
    for ii in range(3):
        for j in range(3):
            if grid[ii+x][j+y] == i:
                # print("Inbox True")
                return True
    return False


def print_grid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print()


def findEmpty(grid,l):
    # print("FindEmpty")
    for row in range(9):
        for col in range(9):
            if (grid[row][col]==0):
                l[0] = row
                l[1] = col
                # print(l[0],l[1])
                return True
    return False


def solve(grid):
    # print("solve")
    l = [0, 0]
    if not (findEmpty(grid, l)):
        return True


    row = l[0]
    col = l[1]

    for i in range(1, 10):
        # print("i ", i)
        if isSafe(grid, row, col, i):
            # print("IsSafe")
            grid[row][col] = i
            if solve(grid):
                return True
            grid[row][col] = 0
    return False


if __name__ == "__main__":
    grid = [[0 for x in range(9)] for y in range(9)]

    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    # grid=[[5,9,6,0,0,0,1,0,0,],
    #       [0,0,0,0,4,0,0,5,0],
    #       [0,0,0,0,0,5,8,0,0],
    #       [3,0,0,5,0,1,0,8,0],
    #       [0,0,0,2,7,3,0,4,5],
    #       [0,0,5,0,0,4,3,1,9],
    #       [7,1,0,3,5,2,0,0,8],
    #       [0,0,0,4,0,7,5,0,1],
    #       [0,5,0,0,1,9,0,0,7]]
    # grid=[[0, 0, 2, 0, 0, 0, 5, 0, 0],
    #       [4, 0, 0, 0, 0, 8, 0, 0, 6],
    #       [0, 8, 0, 4, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 4],
    #       [0, 9, 0, 0, 1, 2, 0, 5, 0],
    #       [0, 7, 0, 0, 0, 0, 0, 9, 0],
    #       [0, 0, 0, 0, 4, 0, 0, 0, 3],
    #       [0, 0, 1, 6, 0, 0, 8, 0, 0],
    #       [0, 0, 6, 0, 3, 9, 0, 0, 0]]
    #
    # grid=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #       [0, 0, 0, 0, 0, 0, 0, 0, 0]]


    if (solve(grid)):
        print_grid(grid)
    else:
        print("Not solvable")

#
#   3 1 6 5 7 8 4 9 2
#   5 2 9 1 3 4 7 6 8
#   4 8 7 6 2 9 5 3 1
#   2 6 3 4 1 5 9 8 7
#   9 7 4 8 6 3 1 2 5
#   8 5 1 7 9 2 6 4 3
#   1 3 8 9 4 7 2 5 6
#   6 9 2 3 5 1 8 7 4
#   7 4 5 2 8 6 3 1 9
