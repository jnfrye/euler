import sympy


# -----Euler Problem 3-----
# What is the largest prime factor of the number 600851475143 ?

def largest_prime_factor(limit):

    p = sympy.primefactors(limit)

    return max(p)
