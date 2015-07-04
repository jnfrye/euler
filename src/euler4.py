import integers


# -----Euler Problem 4-----
# Find the largest palindrome made from the product of two 3-digit numbers.

def largest_product_palindrome(digits=3):
    # Returns the largest palindrome that is the product of two numbers with <digits> digits

    factors = range(10 ** (digits - 1), 10 ** digits)[::-1]
    pal_list = []

    for f1 in factors:
        for f2 in factors:
            product = f1 * f2
            if integers.is_palindrome(product):
                pal_list.append(product)
        factors.remove(f1)

    return max(pal_list)


print "The largest palindrome made from the product of two 3-digit numbers is", largest_product_palindrome()
