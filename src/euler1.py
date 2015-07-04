import integers


# -----Euler Problem 1-----
# Find the sum of all the multiples of 3 or 5 below 1000.


def sum_of_several_multiples(limit, divs=[3, 5]):
    # returns sum of multiples of each element of <divs> up to <limit>
    # entries of <divs> must not include duplicates, and must be prime

    s = 0                               # init. sum
    for n in divs:
        s += integers.sum_of_multiples(limit - 1, n)  # minus 1, we don't count limit

    # get all of the mutual products of divs to remove overcounting
    prods = integers.list_of_products(divs)

    for n in prods:
        s -= integers.sum_of_multiples(limit - 1, n)  # minus 1, we don't count limit

    return s


print "Sum of all the multiples of 3 or 5 below 1000 is", sum_of_several_multiples(1000)
