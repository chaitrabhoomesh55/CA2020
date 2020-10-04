# Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8.


def count_pair(x, n, sum):
    for i in range(0, n):
        temp= sum - x[i]
        if ( temp in x ):
            # print( "pair of numbers whose sum is equal to 8:")
            print(x[i], temp)
          

x=[1,2,3,4,5,6,7,8,9,-1]
n = len(x)
sum=8
count_pair(x, n, sum)

        
