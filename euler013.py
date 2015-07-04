import os

# -----Euler Problem 1-----
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers (data/euler13_data.txt)


os.chdir(str(os.getcwd()))

with open("data/euler13_data.txt", 'r') as f:
    lines = f.readlines()

s = 0
for x in range(0, len(lines)):
    lines[x] = int(lines[x])
    s += lines[x]

print "The sum is", s
