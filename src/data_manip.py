# ******** DATA MANIPULATION MODULE ********
# The following are functions useful for file input/output

import os


def extract_numbers_from_file(f_name, f_dir, delim=' '):
    # This will take a text file of numbers and output a 2D list of those numbers
    #
    # ARGUMENTS: f_name (string)         name of file
    #            f_dir  (string)         directory file is in
    #            delim  (string)         delimiter used to split up numbers into columns
    #
    # RETURNS:   lines (2D int list)     2D list of numbers in the file
    #
    # NOTES:     This will only work for files containing integers! (for now)

    os.chdir(f_dir)

    with open(f_name, 'r') as f:
        lines = f.readlines()

    for x in range(0, len(lines)):
        lines[x] = lines[x][0:lines[x].find('\n')]
        lines[x] = lines[x].split(delim)

        for y in range(0, len(lines[x])):
            lines[x][y] = int(lines[x][y])

    return lines
