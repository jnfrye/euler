# -----Euler Problem 8-----
#
# 73167176531330624919225119674426574742355349194934
# 96983520312774506326239578318016984801869478851843
# 85861560789112949495459501737958331952853208805511
# 12540698747158523863050715693290963295227443043557
# 66896648950445244523161731856403098711121722383113
# 62229893423380308135336276614282806444486645238749
# 30358907296290491560440772390713810515859307960866
# 70172427121883998797908792274921901699720888093776
# 65727333001053367881220235421809751254540594752243
# 52584907711670556013604839586446706324415722155397
# 53697817977846174064955149290862569321978468622482
# 83972241375657056057490261407972968652414535100474
# 82166370484403199890008895243450658541227588666881
# 16427171479924442928230863465674813919123162824586
# 17866458359124566529476545682848912883142607690042
# 24219022671055626321111109370544217506941658960408
# 07198403850962455444362981230987879927244284909188
# 84580156166097919133875499200524063689912560717606
# 05886116467109405077541002256983155200055935729725
# 71636269561882670428252483600823257530420752963450
#
# Find the thirteen adjacent digits in the above 1000-digit number that have the greatest product.
# What is the value of this product?


import os

def extract_numbers_from_file(f_name, f_dir, delim=' '):

    # This will take a text file of numbers and output a 2D list of those numbers
    #
    # ARGUMENTS:
    #           f_name (string)         name of file
    #           f_dir  (string)         directory file is in
    #           delim  (string)         delimiter used to split up numbers into columns
    #
    # RETURNS:
    #           lines (2D int list)     2D list of numbers in the file
    #
    # NOTES:
    #           This will only work for files containing integers! (for now)

    os.chdir(f_dir)

    with open(f_name, 'r') as f:
        lines = f.readlines()

    for x in range(0, len(lines)):
        lines[x] = lines[x][0:lines[x].find('\n')]
        lines[x] = lines[x].split(delim)

        for y in range(0, len(lines[x])):
            lines[x][y] = int(lines[x][y])

    return lines


def number_to_array(input_number):
    #TODO: Rename this to "digits_to_array()"

    # This will take a single number and return its digits as a list
    #
    # ARGUMENTS:
    #           input_number (int)      the number to be split up
    #
    # RETURNS:
    #           arr (int list)          list of digits of input_number

    arr = []

    while input_number > 0:
        arr.append(int(input_number % 10))
        input_number = input_number / 10

    return arr


def max_list_product(input_list, dig_num=13):

    # This will take a list of numbers and return the largest product of adjacent numbers
    #
    # ARGUMENTS:
    #           input_list (int list)        the list of numbers to analyze
    #           dig_num   (int)             how many adjacent numbers to analyze the product of
    #
    # RETURNS:
    #           high_prod (int)             the largest product of adjacent numbers

    # initializations
    high_prod    = 0
    current_spot = 0
#   hp_spot      = 0   not used yet

    digits = []

    # Iterate until you reach the end of input_list
    while current_spot + dig_num < len(input_list):

        # Gather digits to be analyzed
        for x in range(current_spot, current_spot + dig_num):
            digits.append(input_list[x])

        # Skip past zeroes; they never yield highest product
        if 0 in digits:
            current_spot += digits.index(0) + 1

        else:
            product = 1

            for x in digits:
                product *= x

                if product > high_prod:
                    high_prod = product
                    # hp_spot = current_spot #TODO This is not used currently; eventually can return this

            current_spot += 1

        digits = []

    return high_prod
