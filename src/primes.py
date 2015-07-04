import sympy


# ******** PRIME NUMBER MODULE ********
# The following are functions useful for prime number analysis

def largest_prime_factor(limit):

    p = sympy.primefactors(limit)

    return max(p)


def prime(n=6):
    # returns the <n>th prime number
    # pretty slow...

    p = 3
    primes = [2, p]

    if n == 1:
        p = 2

    else:
        while len(primes) < n:
            p += 2
            is_prime = True
            for x in primes:
            # TODO should only check against primes that are <= sqrt (p)
                if p % x == 0:
                    is_prime = False

            if is_prime:
                primes.append(p)

    return p


def prime_sum(limit=2000000):
    # Returns sum of all primes that are less than <limit>

    s = 0

    for p in sympy.sieve.primerange(1, limit):
        s += p

    return s
