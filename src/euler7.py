# -----Euler Problem 7-----
# What is the 10 001st prime number?


def prime(n=6):
    # returns the <n>th prime number

    p = 3
    primes = [2, p]

    if n == 1:
        p = 2

    else:

        while len(primes) < n:
            p += 2
            is_prime = True
            for x in primes:
            # To be more efficient, should only check against primes that are <= sqrt (p)
                if p % x == 0:
                    is_prime = False
            if is_prime:
                primes.append(p)

    return p
