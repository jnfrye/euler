import os


#TODO: put into functions

os.chdir(str(os.getcwd()))

with open("euler13dataz.txt", 'r') as f:
    lines = f.readlines()

s = 0
for x in range(0, len(lines)):
    lines[x] = int(lines[x])
    s += lines[x]

print lines
print s
