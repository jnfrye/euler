# -----Euler Problem 3-----
# What is the largest prime factor of the number 600851475143 ?

from sympy import primefactors


def largest_prime_factor(limit):
    p = primefactors(limit)

    return max(p)
