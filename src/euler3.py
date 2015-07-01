# -----Euler Problem 3-----
# What is the largest prime factor of the number 600851475143 ?

import sympy


def largest_prime_factor(limit):

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


    p = sympy.primefactors(limit)

    return max(p)
