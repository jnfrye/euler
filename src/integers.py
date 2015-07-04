# ******** INTEGERS MODULE ********
# The following functions are useful for integer analysis and manipulation

import list_manip


def sum_of_multiples(lim, div):
    # This function calculates the sum of multiples of <div> up to <lim> using
    # Gauss' trick.

    quo = lim / div
    s = div * quo * (quo + 1) / 2      # Gauss' trick

    return s


def list_of_products(vector):
    # Returns a list of all possible products between elements of <vector>

    table = list_manip.truth_table(len(vector)) # XXX GOTTA GRAB DIS

    for row_num in range(0, len(table)):
        for col_num in range(0, len(table[row_num])):
            # each column is multipled by the corresponding vector element
            table[row_num][col_num] *= vector[col_num]
            # if it was zero, make it one, so when we multiply rows we don't
            # get zero
            if not table[row_num][col_num]:
                table[row_num][col_num] += 1

    prod_vector = [1] * len(table)        # init. vector of ones

    n = 0
    for row in table:
        for col in row:
            prod_vector[n] *= col
        n += 1

    # get rid of the entries of vector and 1 from prod_vector
    prod_vector.remove(1)
    for num in vector:
        prod_vector.remove(num)

    return prod_vector
