# ******** LIST MANIPULATION MODULE ********
# The following functions are useful for list manipulation


def extract_diagonals(matrix, min_len=4):
    # Returns a list of lists of the diagonals of <matrix> (not necessarily square)
    # with at least <min_len> elements

    diag_list = []
    row_len = len(matrix)
    col_len = len(matrix[0])

    for diag in range(0, row_len + col_len - 2 * min_len + 1):
        diag_list.append([])

        row_min = min(diag + (min_len - 1), row_len - 1)
        col_min = min(diag + (min_len - 1), col_len - 1)

        row_max = max(0, diag + (min_len - 1) - (row_len - 1))  # I feel like there's a slicker way to do this?
        col_max = max(0, diag + (min_len - 1) - (col_len - 1))

        for elem in range(0, row_min - row_max + 1):
            diag_list[diag].append(matrix[row_min - elem][col_max + elem])

    return diag_list


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


def max_grid_product(grid, factors=4):
    # Returns the largest product between <factors> adjacent numbers in each list in list of lists <grid>

    high_prod = 0

    for row in grid:
        row_high_prod = max_list_product(row, factors)
        if row_high_prod > high_prod:
            high_prod = row_high_prod

    return high_prod


def max_list_product(input_list, dig_num=13):
    # This will take <input_list> of numbers and return the largest product of <dig_num> adjacent numbers
    #
    # ARGUMENTS: input_list (int list)        the list of numbers to analyze
    #            dig_num   (int)             how many adjacent numbers to analyze the product of
    #
    # RETURNS:   high_prod (int)             the largest product of adjacent numbers

    # initializations
    high_prod    = 0
    current_spot = 0
#   hp_spot      = 0   not used yet

    digits = []

    # Iterate until you reach the end of input_list
    while current_spot + dig_num < len(input_list):

        # Gather digits to be analyzed
        for x in range(current_spot, current_spot + dig_num):
            digits.append(input_list[x])

        # Skip past zeroes; they never yield highest product
        if 0 in digits:
            current_spot += digits.index(0) + 1

        else:
            product = 1

            for x in digits:
                product *= x

                if product > high_prod:
                    high_prod = product
                    # hp_spot = current_spot #TODO This is not used currently; eventually can return this

            current_spot += 1

        digits = []

    return high_prod


def matrix_display(matrix):
    # prints out list of lists <matrix> row by row
    # TODO make it so that things are nicely columnated

    for row in matrix:
        for col in row:
            print str(col),
        print '\n'


def transpose(matrix):
    return map(lambda *a: list(a), *matrix)    # lambda calculus magic
