# -----Euler Problem 6-----
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def square_sum_difference(limit=10):

    # TODO: FILL THIS OUT
    #
    # ARGUMENTS:
    #           f_name (string)         name of file
    #
    # RETURNS:
    #           lines (2D int list)     2D list of numbers in the file
    #
    # NOTES:
    #           This will only work for files containing integers! (for now)
    # TODO


    # Sum from one to limit is an arithmetic series:
    s = limit * (limit + 1) / 2

    # Sum of squares is a 'square pyramidal number':
    sq_s = limit * (limit + 1) * (2 * limit + 1) / 6

    return s ** 2 - sq_s
