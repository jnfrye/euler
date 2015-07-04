import euler8
import os

tri = euler8.extract_numbers_from_file("euler18data.txt", str(os.getcwd()))

last_row = len(tri)

for row in reversed(range(0, last_row)):
    for col in range(0, len(tri[row]) - 1):
        tri[row - 1][col] += max(tri[row][col], tri[row][col + 1])
