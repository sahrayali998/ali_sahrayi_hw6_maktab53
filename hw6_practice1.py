from functools import reduce
import math
li = [2, 68, 9, 0, 13]
q = list(map(lambda x: math.sqrt(x), li))
print(sum(q))
s = reduce(lambda x,y: math.sqrt(x) + y, li)
print(s)
