# -----Euler Problem 6-----
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sq_of_sum_minus_sum_of_sq(limit=10):
    # Sum from one to limit is an arithmetic series:
    s = limit*(limit + 1) / 2

    # Sum of squares is a 'square pyramidal number':
    sq_s = limit*(limit + 1)*(2*limit + 1) / 6
    
    return s**2 - sq_s

