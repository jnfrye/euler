# -----Euler Problem 4-----
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindrome(number):
    # Tests whether <number> is a palindrome, returns BOOL

    num_string = str(number)
    reverse = int(num_string[::-1])

    return reverse - number == 0


def times_table(digits):
    # Returns a multiplication table for every number with <digits> digits

    factors = range(10 ** (digits - 1), 10 ** digits)[::-1]
    times_tab = []
    row = []

    for f1 in factors:
        for f2 in factors:
            product = f1 * f2
            row.append(product)
        times_tab.append(row)
        row = []

    return times_tab


def largest_product_palindrome(digits):
    # Returns the largest palindrome that is the product of two numbers with <digits> digits

    factors = range(10 ** (digits - 1), 10 ** digits)[::-1]
    pal_list = []

    for f1 in factors:
        for f2 in factors:
            product = f1 * f2
            if is_palindrome(product):
                pal_list.append(product)
        factors.remove(f1)

    return max(pal_list)
