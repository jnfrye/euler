# -----Euler Problem 9-----
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def special_pythagorean_triplet():

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



    for b in range(1, 500 / 2):
        a = 1000 * (500. - b) / (1000 - b)
        if a % 1 == 0:
            triplets = [int(a), int(b), int(1000 - a - b)]

    return triplets
