# ******** LIST MANIPULATION MODULE ********
# The following functions are useful for list manipulation


def truth_table(n):
    # generates a table of alternating ones and zeroes in truth table fashion
    # example: for n = 2, returns
    # 1 1
    # 0 1
    # 1 0
    # 0 0

    table = []
    col = []

    for row_num in range(0, 2 ** n):
        for col_num in range(0, n):
            if (row_num / 2 ** col_num) % 2 == 0:
                col.append(1)
            else:
                col.append(0)
        table.append(col)
        col = []

    return table


def matrix_display(matrix):
    # prints out list of lists <matrix> row by row
    # TODO make it so that things are nicely columnated

    for row in matrix:
        for col in row:
            print str(col),
        print '\n'
