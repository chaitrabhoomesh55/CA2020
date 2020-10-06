# 4. Write a program that accepts a hyphen-separated sequence of words 
# as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.


def sort_list(h):
    items= [n for n in h.split('-')]
    items.sort()
    print('-'.join(items))

h = input("enter hyphen seaparated values:")
sort_list(h)
