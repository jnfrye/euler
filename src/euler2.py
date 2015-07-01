# -----Euler Problem 2-----
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.


def sum_of_even_fib(limit):


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


    f = [1, 2]      # first two fibonacci numbers
    n = 1
    s = 0           # initialize sum to zero

    while f[n] < limit:
        f.append(f[n] + f[n - 1])   # add the next fib. num. to end of list
        if f[n] % 2 == 0:
            s += f[n]               # add it to the sum if it's even
        n += 1                      # iterate

    return s
