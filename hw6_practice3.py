from functools import reduce
numbers = [10,-10,40,90,-15]
import math
# max_num = reduce(lambda x,y: x if x > y ,numbers)
max_num = reduce(lambda x,y: max(numbers),numbers)
min_num = reduce(lambda x,y : min(numbers),numbers)
print(max_num,min_num)