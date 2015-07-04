# -----Euler Problem 2-----
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.


def sum_of_even_fib(limit):

    f = [1, 2]      # first two fibonacci numbers
    n = 1
    s = 0           # initialize sum to zero

    while f[n] < limit:
        f.append(f[n] + f[n - 1])   # add the next fib. num. to end of list
        if f[n] % 2 == 0:
            s += f[n]               # add it to the sum if it's even
        n += 1                      # iterate

    return s
