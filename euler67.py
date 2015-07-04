import os

import src.data_manip as data_manip

# -----Euler Problem 67-----
# Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
# a 15K text file containing a triangle with one-hundred rows.

tri = data_manip.extract_numbers_from_file("euler67_data.txt", str(os.getcwd()) + "/data")

last_row = len(tri)

for row in reversed(range(0, last_row)):
    for col in range(0, len(tri[row]) - 1):
        tri[row - 1][col] += max(tri[row][col], tri[row][col + 1])

print "The maximum sum from top to bottom of the triangle in euler67_data.txt is", tri[0][0]
