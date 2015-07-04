import sympy

import list_manip


# ******** INTEGERS MODULE ********
# The following functions are useful for integer analysis and manipulation

def is_palindrome(number):
    # Returns True if <number> is a palindrome

    num_string = str(number)
    reverse = int(num_string[::-1])

    return reverse - number == 0


def least_common_multiple(divisors=range(1, 21)):
    # Returns least common multiple of INTs in <divisors>

    # No matter the divisors, we at least need the max divisor as an LCM
    lcm = max(divisors)
    lcm_factors = sympy.factorint(lcm)

    for n in divisors:
        n_factors = sympy.factorint(n)

        for f in n_factors:

            # If this factor appears in the LCM ...
            if f in lcm_factors:
                factor_excess = lcm_factors[f] - n_factors[f]

                # ... check if there are enough of them
                if factor_excess < 0:

                    # If not, we multiply into LCM to account for this
                    lcm *= - factor_excess * f
                    lcm_factors[f] += - factor_excess

            # If this factor does not appear in the LCM, multiple into LCM
            else:
                lcm *= n_factors[f] * f
                lcm_factors[f] = n_factors[f]

    return lcm


def list_of_fibonacci(limit):
    # Returns list of fibonacci numbers below <limit>

    f = [1, 2]      # first two fibonacci numbers
    n = 1           # iterator

    while f[n] < limit:
        f.append(f[n] + f[n - 1])   # add the next fib. num. to end of list
        n += 1                      # iterate

    return f


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


def sum_of_multiples(lim, div):
    # This function calculates the sum of multiples of <div> up to <lim> using
    # Gauss' trick.

    quo = lim / div
    s = div * quo * (quo + 1) / 2      # Gauss' trick

    return s


def times_table(digits):
    # Returns a multiplication table for every number with <digits> digits

    factors = range(10 ** (digits - 1), 10 ** digits)[::-1]
    times_tab = []
    row = []

    for f1 in factors:
        for f2 in factors:
            product = f1 * f2
            row.append(product)
        times_tab.append(row)
        row = []

    return times_tab
