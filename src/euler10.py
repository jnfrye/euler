# -----Euler Problem 10-----
#
# Find the sum of all the primes below two million.

from sympy import sieve


def prime_sum(limit=2000000):


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


    s = 0

    for p in sieve.primerange(1, limit):
        s += p

    return s
