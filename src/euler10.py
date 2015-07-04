# -----Euler Problem 10-----
#
# Find the sum of all the primes below two million.




def prime_sum(limit=2000000):
    # Returns sum of all primes that are less than <limit>

    from sympy import sieve

    s = 0

    for p in sieve.primerange(1, limit):
        s += p

    return s
