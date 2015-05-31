# -----Euler Problem 1-----
# Find the sum of all the multiples of 3 or 5 below 1000.

# First solution:
# def sum_of_multiples(limit):
#
#     s = 0           # initialize sum to zero
#
#     for n in range(1, limit):
#         if n % 3 == 0 or n % 5 == 0:    # test if it is a multiple of 3 or 5
#             s += n
#
#     return s
#
# This solution can be improved as follows:


def sum_of_multiples(lim, div):
    # This function calculates the sum of multiples of "div" until "lim" using
    # Gauss' trick.
    quo = lim/div                      # How many div's are in lim?
    s = div * quo * (quo + 1) / 2      # Gauss' trick

    return s


def two_d_truth_table(n):
    # generates a table of alternating ones and zeroes
    # example: for n=2, returns
    # 1 1
    # 0 1
    # 1 0
    # 0 0
    table = []
    col = []

    for row_num in range(0, 2**n):
        for col_num in range(0, n):
            if (row_num / 2**col_num) % 2 == 0:
                col.append(1)
            else:
                col.append(0)
        table.append(col)
        col = []

    return table


def two_d_table_display(table):
    # prints out a two-D table row by row
    for row in table:
        for col in row:
            print str(col),
        print '\n'


def list_of_products(vector):
    # returns a list of all possible products between elements of vector

    table = two_d_truth_table(len(vector))

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


def sum_of_several_multiples(limit, divs=[3, 5]):
    # returns sum of multiples of each element of divs up to limit
    # entries of divs must not include duplicates, and must be prime

    s = 0                               # init. sum
    for n in divs:
        s += sum_of_multiples(limit - 1, n) # minus 1, we don't count limit

    # get all of the mutual products of divs to remove overcounting
    prods = list_of_products(divs)

    for n in prods:
        s -= sum_of_multiples(limit - 1, n) # minus 1, we don't count limit

    return s
