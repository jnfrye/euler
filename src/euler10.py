# -----Euler Problem 10-----
#
# Find the sum of all the primes below two million.

from sympy import sieve

def prime_sum(limit=2000000):

    s = 0

    for p in sieve.primerange(1, limit):
        s += p

    return s
