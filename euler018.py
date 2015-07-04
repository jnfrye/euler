import os

import src.data_manip as data_manip

# -----Euler Problem 18-----
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle in euler18_data.txt

tri = data_manip.extract_numbers_from_file("euler18_data.txt", str(os.getcwd()) + "/data")

last_row = len(tri)

for row in reversed(range(0, last_row)):
    for col in range(0, len(tri[row]) - 1):
        tri[row - 1][col] += max(tri[row][col], tri[row][col + 1])

print "The maximum sum from top to bottom of the triangle in euler18_data.txt is", tri[0][0]
