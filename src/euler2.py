# -----Euler Problem 2-----
# By considering the terms in the Fibonacci sequence whose values do not exceed
# four million, find the sum of the even-valued terms.

import integers


print "The sum of even Fibonacci numbers less than 4M is", \
      sum([x for x in integers.list_of_fibonacci(4000000) if x % 2 == 0])
