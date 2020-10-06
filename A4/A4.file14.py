
14. What is the output of the following codes:


def foo():
    try:
       return 1
    finally:
        return 2

k = foo()
print(k)


# Output: 2


def a():
    try:
        f(x, 4)
    finally:
        print('after f')
    print('after f?')

a()

# output:
# after f
# Traceback (most recent call last):
#   File "c:/Users/ADMIN/chai/python_codes/TP.py", line 24, in <module>
#     a()
#   File "c:/Users/ADMIN/chai/python_codes/TP.py", line 17, in a
#     f(x, 4)
# TypeError: 'int' object is not callable