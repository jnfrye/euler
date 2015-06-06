import sys
sys.path.append("/home/jfrye/Dropbox/Jamison_Josh_Shared_UBUNTU/Programming/Python/euler/src")

import euler1
import euler2
import euler3
import euler4
import euler5
import euler6
import euler7
import euler8
import euler9


t = euler9.special_pythagorean_triplet()

p = 1
for x in t:
    p *= x

print p
    
