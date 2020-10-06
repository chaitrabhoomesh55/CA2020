# 13. Flatten the list [[1,2,3],[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
# Goal : Turn [1,2,3,4,5,6,7] to 1234567 


# From functools import *
import functools

x= [[1,2,3],[4,5],[6,7,8]]

endstring = functools.reduce(lambda a, b: a+b, x)
print(endstring)

delimeter = ''
finalstr = functools.reduce(lambda a, b: str(a) + delimeter + str(b), endstring)
print(finalstr)
