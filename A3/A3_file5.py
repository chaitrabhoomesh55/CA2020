
5.


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
for i in x:
    if (i % 2) == 0:
        print("i is even")
        x.remove(i)
        print("the list after removing the even numbers:")
print(x)


# ---using Slicing DS:-
# x[::2]
# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
