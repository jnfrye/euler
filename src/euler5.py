# -----Euler Problem 5-----
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import sympy

# This new method is faster by a factor of ~63 for the default arg!


def least_common_multiple(divisors=range(1, 21)):

    # No matter the divisors, we at least need the max divisor as an LCM
    lcm = max(divisors)
    lcm_factors = sympy.factorint(lcm)

    for n in divisors:
        n_factors = sympy.factorint(n)

        for f in n_factors:

            # If this factor appears in the LCM ...
            if f in lcm_factors:
                factor_excess = lcm_factors[f] - n_factors[f]

                # ... check if there are enough of them
                if factor_excess < 0:

                    # If not, we multiply into LCM to account for this
                    lcm *= - factor_excess * f
                    lcm_factors[f] += - factor_excess

            # If this factor does not appear in the LCM, multiple into LCM
            else:
                lcm *= n_factors[f] * f
                lcm_factors[f] = n_factors[f]

    return lcm

# OLD METHOD:

# def least_common_multiple(divisors=range(1,21)):
#     lcm = 0                 # initialize lcm = 0
#     is_lcm = False          # initialize test to false
#     gcd = max(divisors)     # greatest common divisor

#     while not is_lcm:
#         lcm += gcd          # increment by gcd since the lcm must be a multiple of it
#         is_lcm = True

#         for d in divisors:
#             if lcm % d != 0:
#                 is_lcm = False

#     return lcm
