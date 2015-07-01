# -----Euler Problem 5-----
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import sympy

# This new method is faster by a factor of ~63 for the default arg!


def least_common_multiple(divisors=range(1, 21)):

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
