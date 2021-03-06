# -----Euler Problem 9-----
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def special_pythagorean_triplet():
    # Returns the Pythagorean triplet that sums to 1000

    for b in range(1, 500 / 2):
        a = 1000 * (500. - b) / (1000 - b)
        if a % 1 == 0:
            triplets = [int(a), int(b), int(1000 - a - b)]

    return triplets

prod = 1
for x in special_pythagorean_triplet():
    prod *= x

print "The product of the Pythagorean triplet whose sum is 1000 is", prod
